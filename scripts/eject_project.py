import argparse
import subprocess
import shutil
import os
import sys

def run_command(command, cwd=None):
    """
    シェルコマンドを実行し、標準出力を返す。
    
    Args:
        command (str): 実行するコマンド
        cwd (str, optional): カレントディレクトリ
    """
    try:
        result = subprocess.run(
            command, cwd=cwd, check=True, text=True, capture_output=True, shell=True
        )
        print(f"COMMAND: {command}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"ERROR executing: {command}")
        print(e.stderr)
        raise

def copy_framework_files(target_dir):
    """
    Maestroフレームワークの構成ファイルを独立したプロジェクトのルートにコピーする。
    """
    maestro_root = os.getcwd()
    
    # コピー対象のファイル/ディレクトリリスト
    # Note: .git, projects/, scripts/ 等は除外する
    framework_items = [
        "AGENTS.md",
        "manual.md",
        "agents",
        ".agent",
        "knowledge",
        "docs/standards",
        "docs/templates",
        ".github"
    ]

    print("--- フレームワークファイルのコピー開始 ---")
    for item in framework_items:
        src_path = os.path.join(maestro_root, item)
        dst_path = os.path.join(target_dir, item)
        
        if os.path.exists(src_path):
            if os.path.isdir(src_path):
                # shutil.copytree はコピー先が存在しないことを前提とするため、存在チェックを行う
                # プロジェクトフォルダ内に既に同名のディレクトリがある場合はマージコピーを行う
                if os.path.exists(dst_path):
                    print(f"警告: {item} は既にターゲットに存在します。上書き/マージします...")
                    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                else:
                    shutil.copytree(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)
            print(f"Copied: {item}")
        else:
            print(f"警告: ソース {item} が見つかりません。スキップします。")

def eject_project(project_name, new_repo_url):
    """
    プロジェクトをMaestroから独立させる（Eject）。
    Git Subtreeを使用して履歴を保持したまま分離し、フレームワークファイルを注入する。
    """
    project_path = os.path.join("projects", project_name)
    if not os.path.exists(project_path):
        print(f"エラー: プロジェクトディレクトリ '{project_path}' が存在しません。")
        sys.exit(1)

    branch_name = f"eject/{project_name}"
    
    print(f"*** Ejecting Phase 1: Git Subtree Split ({project_name}) ***")
    # 1. サブツリー分割（履歴の切り出し）
    prefix = f"projects/{project_name}"
    run_command(f"git subtree split --prefix={prefix} -b {branch_name}")

    print(f"*** Ejecting Phase 2: 一時リポジトリの準備 ***")
    # 2. 一時ディレクトリへのクローン
    temp_dir = os.path.abspath(f"temp_eject_{project_name}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    run_command("git init", cwd=temp_dir)
    
    # 親リポジトリ（現在のディレクトリ）のsplitブランチからpull
    parent_repo_path = os.getcwd()
    parent_repo_path = parent_repo_path.replace("\\", "/") # Windows対応
    
    print(f"{parent_repo_path} のブランチ {branch_name} からプルします...")
    run_command(f"git pull \"{parent_repo_path}\" {branch_name}", cwd=temp_dir)

    print(f"*** Ejecting Phase 3: Maestroフレームワークの注入 ***")
    copy_framework_files(temp_dir)
    
    print(f"*** Ejecting Phase 4: コミットとプッシュ準備 ***")
    run_command("git add .", cwd=temp_dir)
    try:
        run_command("git commit -m \"chore: eject project from Maestro framework\"", cwd=temp_dir)
    except Exception:
        print("コミットする変更がありません（フレームワークファイルが既存と同一の可能性があります）。続行します。")

    run_command(f"git remote add origin {new_repo_url}", cwd=temp_dir)
    
    print(f"プッシュ先: {new_repo_url}")
    print(f"プッシュ準備完了: git push -u origin main (ディレクトリ: {temp_dir})")
    
    # 安全のため、実際のPushはコメントアウトまたはtry実行で失敗許容する形にする
    # spec通り自動でPushを試みる
    try:
        run_command("git push -u origin main", cwd=temp_dir)
    except Exception as e:
        print(f"プッシュに失敗しました（URLがダミーの場合は正常な動作です）: {e}")
        print("以下のディレクトリで手動確認・プッシュを行ってください: " + temp_dir)

    print("完了しました。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maestroからプロジェクトを独立したリポジトリとして切り出します。")
    parser.add_argument("project_name", help="projects/ 内のプロジェクトディレクトリ名")
    parser.add_argument("repo_url", help="新しいリモートリポジトリのURL")
    
    args = parser.parse_args()
    
    eject_project(args.project_name, args.repo_url)
