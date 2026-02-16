import argparse
import subprocess
import shutil
import os
import sys

def run_command(command, cwd=None):
    """
    シェルコマンドを実行し、標準出力を返す。
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
        # git subtree add の失敗（マージ競合など）では中断する
        raise

def inject_project(project_name, repo_url, branch="main"):
    """
    独立したリポジトリをMaestroプロジェクトとして再取り込み（Inject）する。
    """
    maestro_root = os.getcwd()
    project_dir = os.path.join(maestro_root, "projects", project_name)
    
    print(f"*** Injection Phase 1: リモート追加とサブツリー取り込み ***")
    
    remote_name = f"ejected-{project_name}"
    
    # 既存のリモートがあれば削除
    try:
        run_command(f"git remote remove {remote_name}")
    except:
        pass
        
    run_command(f"git remote add {remote_name} {repo_url}")
    run_command(f"git fetch {remote_name}")
    
    prefix = f"projects/{project_name}"
    
    # Subtree add
    # 履歴を1つにまとめる (--squash) かどうか。仕様に基づき squash をデフォルトとする。
    try:
        run_command(f"git subtree add --prefix={prefix} {remote_name} {branch} --squash")
    except subprocess.CalledProcessError:
        print("Subtree add に失敗しました。プレフィックスが既に存在するため、'pull' を試みます...")
        # プロジェクトディレクトリが存在する場合は pull で更新
        run_command(f"git subtree pull --prefix={prefix} {remote_name} {branch} --squash")

    print(f"*** Injection Phase 2: フレームワークファイルのクリーンアップ ***")
    
    # フレームワーク由来のファイルは、Maestro側で管理するため重複削除する
    redundant_files = [
        "AGENTS.md",
        "manual.md",
        "agents",
        ".agent",
        "docs/standards", # directory
        ".github" # directory
    ]
    
    for item in redundant_files:
        path_to_remove = os.path.join(project_dir, item)
        if os.path.exists(path_to_remove):
            print(f"不要なフレームワークファイルを削除: {path_to_remove}")
            if os.path.isdir(path_to_remove):
                shutil.rmtree(path_to_remove)
            else:
                os.remove(path_to_remove)
                
    print(f"*** Injection Phase 3: 知見のマージ (手動確認) ***")
    
    project_knowledge_dir = os.path.join(project_dir, "knowledge")
    maestro_knowledge_dir = os.path.join(maestro_root, "knowledge")
    
    if os.path.exists(project_knowledge_dir):
        print(f"プロジェクト内に knowledge ディレクトリが見つかりました: {project_knowledge_dir}")
        print(f"以下のディレクトリと手動で比較・統合を行ってください: {maestro_knowledge_dir}")
        
        # 簡易Diffレポート
        project_files = set(os.listdir(project_knowledge_dir))
        for f in project_files:
            m_file = os.path.join(maestro_knowledge_dir, f)
            
            if os.path.exists(m_file):
                print(f"[MERGE CHECK] 共通ファイルあり: {f}")
            else:
                print(f"[NEW KNOWLEDGE] 新規ファイル発見: {f}")
    
    print("*** Injection 完了 ***")
    print("'projects/' ディレクトリを確認し、結果をコミットしてください。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="独立したリポジトリをMaestroに再統合します。")
    parser.add_argument("project_name", help="projects/ 内のプロジェクトディレクトリ名")
    parser.add_argument("repo_url", help="独立リポジトリのURL")
    parser.add_argument("--branch", default="main", help="プル対象のブランチ (default: main)")
    
    args = parser.parse_args()
    
    inject_project(args.project_name, args.repo_url, args.branch)
