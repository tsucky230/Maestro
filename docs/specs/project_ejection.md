# プロジェクト独立化（Ejection）機能 仕様書

Maestroリポジトリ内で育成したプロジェクトを、開発完了後やフェーズ移行時に「独立したGitリポジトリ」として切り出す機能の仕様。

## 1. 目的

- `projects/` 配下でインキュベーションしたプロジェクトを、独立したリポジトリ（GitHub等）に履歴付きで移行する。
- 移行先でもMaestroのエージェント機能（自律開発支援）を継続利用できるようにする。

## 2. 独立化（Eject）のフロー

ユーザーは以下のコマンド（またはスクリプト）を実行する想定:
`python scripts/eject_project.py <project_name> <new_repo_url>`

### 処理ステップ

1. **履歴の分離 (Git Subtree)**
    - `projects/<project_name>` ディレクトリの内容を、コミット履歴を含めて抽出する。
    - コマンド: `git subtree split --prefix=projects/<project_name> -b eject/<project_name>`

2. **新リポジトリの準備**
    - 一時ディレクトリに新リポジトリを作成（またはクローン）。
    - `eject/<project_name>` ブランチの内容を新リポジトリのルートにプルする。

3. **フレームワークの移植 (Maestro Core Injection)**
    - 独立後もエージェントが機能するように、Maestroのコアファイルを新リポジトリにコピーする。
    - **コピー対象**:
        - `AGENTS.md` (契約書)
        - `manual.md` (マニュアル)
        - `agents/` (エージェント役割定義)
        - `.agent/` (ワークフロー、MCP設定)
        - `docs/standards/` (標準規約)
        - `docs/templates/` (ドキュメントテンプレート)
        - `.github/` (Copilot Instructions等)

4. **パス・設定の調整**
    - `uv` (pyproject.toml) の依存関係パス修正（もしローカルパス参照があれば）。
    - `AGENTS.md` 内の相対パスリンクの確認（ディレクトリ構成が変わるため、`projects/<name>/` プレフィックスが不要になる箇所の修正）。

5. **初期コミット & プッシュ**
    - "Initial commit from Maestro Ejection" としてコミット。
    - 指定されたリモートURLにプッシュ。

6. **（オプション）元リポジトリのクリーンアップ**
    - Maestroリポジトリから `projects/<project_name>` を削除する（アーカイブ化）。

## 3. 必要なスクリプト構成案

`scripts/eject_project.py`

```python
import argparse
import subprocess
import shutil
import os

def eject_project(project_name, new_repo_url):
    # 1. git subtree split
    subprocess.run(["git", "subtree", "split", "--prefix=projects/" + project_name, "-b", "eject/" + project_name])
    
    # 2. Setup new repo in temp dir
    temp_dir = f"temp_eject_{project_name}"
    os.makedirs(temp_dir)
    subprocess.run(["git", "init"], cwd=temp_dir)
    subprocess.run(["git", "pull", "../", f"eject/{project_name}"], cwd=temp_dir)
    
    # 3. Copy Framework Files
    framework_files = [
        "AGENTS.md", "manual.md", "agents", ".agent", 
        "docs/standards", "docs/templates", ".github"
    ]
    for item in framework_files:
        if os.path.exists(item):
            # Copy item to temp_dir root...
            pass
            
    # 4. Commit and Push
    subprocess.run(["git", "add", "."], cwd=temp_dir)
    subprocess.run(["git", "commit", "-m", "chore: eject project from Maestro framework"], cwd=temp_dir)
    subprocess.run(["git", "remote", "add", "origin", new_repo_url], cwd=temp_dir)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=temp_dir)
    
    print(f"Project {project_name} has been ejected to {new_repo_url}")
```

## 4. 検討事項

- **CI/CD設定**: `.github/workflows` はプロジェクト固有のものとフレームワーク共通のものが混ざっている可能性があるため、選別が必要か？
  - → 基本的にはプロジェクト固有のもの（`projects/<name>/.github`にあれば）優先だが、Maestro標準のCIがあればコピーする。
- **知識ベース (`knowledge/`)**:
  - `knowledge/` は全プロジェクト共通の知見だが、独立後も参照したいか？
  - → **Yes**. `knowledge/` もコピーして、独立後のプロジェクトでも「自律学習」を継続できるようにすべき。

## 5. 結論（仕様）

- **コマンド**: `scripts/eject_project.py` を実装する。
- **動作**:
    1. プロジェクトディレクトリを履歴付きで分離。
    2. Maestroの「エージェント脳（docs/agents/.agent）」を移植。
    3. `knowledge/` も移植して学習サイクルを維持。
    4. 新リポジトリとして独立させる。

## 6. 再取り込み（Injection / Re-integration）仕様

独立して開発が進んだプロジェクトを、次期バージョンの開発のためにMaestroに戻す（里帰りさせる）機能。

### 目的

独立リポジトリで成長したコードと履歴をMaestroに取り込み、Maestroの強力なエージェント支援を受けてアップデートを行う。

### コマンド

`python scripts/inject_project.py <project_name> <repo_url>`

### 処理ステップ

1. **Git Subtree Add/Pull**
    - 指定されたリポジトリを `projects/<project_name>` 配下にサブツリーとして取り込む。
    - コマンド: `git subtree add --prefix=projects/<project_name> <repo_url> <branch> --squash`

2. **フレームワークファイルの除去（Cleanup）**
    - プロジェクト内に含まれているMaestroフレームワークファイル（独立時にコピーしたもの）を削除する。これらはMaestro本体のものが適用されるため不要。
    - 削除対象: `AGENTS.md`, `manual.md`, `agents/`, `.agent/`, `docs/standards/` 等（`projects/<name>/` 直下にあるもの）。

3. **知識の統合（Knowledge Merge）**
    - プロジェクト側で育った `knowledge/`（`projects/<name>/knowledge/`）があれば、Maestro本体の `knowledge/` と比較・統合する。
    - ※ここは競合の可能性があるため、自動マージは行わず「差分レポート」を出力し、人間が判断する。

4. **コンテキストの接続**
    - `projects/<name>/docs/project-context.md` 等が存在すれば、それをMaestroのコンテキストとして認識させる。

### サイクルイメージ

`Maestro (Incubate)` → `Eject` → `Independent Repo (Grow)` → `Inject` → `Maestro (Update)` → `Eject` ...
