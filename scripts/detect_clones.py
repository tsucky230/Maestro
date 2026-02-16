import ast
import os
import sys
import hashlib

def normalize_node(node):
    """
    ASTノードを正規化する（Docstringやコメントを除去したコード文字列を生成するため）。
    本来はASTをトラバースして構造だけ比較するのが正確だが、
    簡易実装として「Docstringを除いた関数本体のソースコード」を比較対象とする。
    """
    # Docstring除去
    if (len(node.body) > 0 and isinstance(node.body[0], ast.Expr) and
        isinstance(node.body[0].value, ast.Constant) and
        isinstance(node.body[0].value.value, str)):
        # 本体がDocstringのみの場合は空になるが、それはそれで「空関数」として検出できる
        processing_body = node.body[1:]
    else:
        processing_body = node.body

    if not processing_body:
        return ""

    # ソースコード生成（unparseはPython 3.9+）
    # 簡易的に、各ステートメントのdump文字列を連結する（変数名の違いなどは無視できない＝完全一致検出）
    # 変数名のリネーム（α変換）まで対応するのは複雑なので、まずは「コピペ」検出を目指す。
    try:
        return ast.unparse(processing_body) # Python 3.9+
    except AttributeError:
        # Fallback for older python (should mostly be 3.9+ now)
        return str([ast.dump(n) for n in processing_body])

def get_function_hashes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            return []

    hashes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # 非常に短い関数（1行など）は除外
            if len(node.body) <= 1: 
                continue
                
            norm_code = normalize_node(node)
            if len(norm_code) < 50: # 短すぎるコードは無視
                continue

            code_hash = hashlib.md5(norm_code.encode("utf-8")).hexdigest()
            hashes.append({
                "file": file_path,
                "name": node.name,
                "line": node.lineno,
                "hash": code_hash,
                "code_preview": norm_code[:100].replace("\n", " ") + "..."
            })
    return hashes

def scan_directory(root_dir):
    all_functions = {}
    
    for root, dirs, files in os.walk(root_dir):
        # .venv, .git, __pycache__ 除外
        dirs[:] = [d for d in dirs if d not in [".venv", ".git", "__pycache__", "output"]]
        
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                funcs = get_function_hashes(path)
                for f in funcs:
                    h = f["hash"]
                    if h not in all_functions:
                        all_functions[h] = []
                    all_functions[h].append(f)
                    
    return all_functions

def report_clones(clones):
    found = False
    print("=== Code Clone Detection Report ===\n")
    for h, entries in clones.items():
        if len(entries) > 1:
            found = True
            print(f"Clone Group (Hash: {h[:8]}) - {len(entries)} locations:")
            for e in entries:
                print(f"  - {e['file']}:{e['line']} (def {e['name']})")
            print(f"  Code: {entries[0]['code_preview']}\n")
            
    if not found:
        print("No clones found.")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Scanning {target_dir} for code clones...")
    results = scan_directory(target_dir)
    report_clones(results)
