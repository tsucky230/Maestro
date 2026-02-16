> 🚀 **このファイルの役割**: ブランチ戦略（main/featureの使い分け）と、プロジェクト開始時の対話的オンボーディング手順を定義します。

# ブランチ戦略・起動時オンボーディング

> このファイルは `AGENTS.md` Section 20 の内容を含みます。

---

## 20. ブランチ戦略・起動時オンボーディング

### mainブランチの役割

**`main` ブランチはMaestroフレームワーク自体を最新に保つための専用ブランチである。** プロジェクトの成果物（設計書、ソースコード、テスト等）を `main` ブランチに直接コミットしてはならない。

```
main ブランチ
  │  ← Maestroフレームワークの更新のみ（AGENTS.md, テンプレート, knowledge/ 等）
  │
  ├── feature/<project>/<description>  ← プロジェクト作業用ブランチ
  ├── review/<project>/<description>   ← レビュー作業用ブランチ
  └── hotfix/<description>             ← フレームワーク修正用ブランチ
```

### ブランチ命名規約

| ブランチ種別 | パターン | 用途 |
|------------|---------|------|
| `feature/<project>/<description>` | `feature/my-app/initial-requirements` | 新規プロジェクト開発 |
| `review/<project>/<description>` | `review/my-app/requirements-review` | 成果物レビュー |
| `hotfix/<description>` | `hotfix/fix-template-typo` | フレームワーク修正 |
| `docs/<description>` | `docs/add-new-checklist` | フレームワークドキュメント更新 |

### 起動時オンボーディング（インタラクティブメニュー）

エージェント起動時（ワークフロー実行時）に、以下のメニューを人間に提示し、何をしたいのかを確認する:

```
🎼 Maestro — ESPR 2.0 ソフトウェア開発エージェント

何をお手伝いしましょうか？

1️⃣  新規プロジェクトを開始する（要求ヒアリングから）
2️⃣  既存プロジェクトの作業を継続する
3️⃣  成果物をレビューする（設計書、コード等）
4️⃣  成果物間の整合性をチェックする
5️⃣  テストを設計・実行する
6️⃣  既存の成果物を閲覧・検索する
7️⃣  フレームワーク自体を更新する（テンプレート、ルール等）

番号で選んでください（または自由にご要望をお伝えください）:
```

### 選択後のフロー

#### 1️⃣ 新規プロジェクト開始

```
1. プロジェクト名を聞く
2. git checkout -b feature/<project>/initial-requirements
3. docs/projects/<project>/ ディレクトリ構成を作成
4. 対話ログを作成
5. Step 1（要求ヒアリング）に進む
```

#### 2️⃣ 既存プロジェクト継続

```
1. docs/projects/ 配下のプロジェクト一覧を表示
2. プロジェクトを選択
3. context/current-phase.md を読み込み、現在の工程を確認
4. 既存のブランチがあればチェックアウト、なければ新規作成
5. 該当工程のステップに進む
```

#### 3️⃣ 成果物レビュー

```
1. レビュー対象のプロジェクト・成果物を聞く
2. git checkout -b review/<project>/<description>
3. 対話ログを作成（工程コード: REV）
4. レビュー観点表を参照しながらレビュー実施
5. レビュー結果をコミット
```

#### 4️⃣ 整合性チェック

```
1. チェック対象のプロジェクト・文書ペアを聞く
2. git checkout -b review/<project>/consistency-check
3. consistency-review.md テンプレートでレポート作成
4. 結果をコミット
```

#### 5️⃣ テスト設計・実行

```
1. テスト対象のプロジェクト・テストレベル（UT/IT/QT）を聞く
2. 既存ブランチをチェックアウト
3. 該当ステップ（Step 4/5/6）に進む
```

#### 6️⃣ 成果物閲覧

```
1. docs/projects/ 配下を一覧表示
2. 指定された成果物を表示（ブランチ作成不要）
```

#### 7️⃣ フレームワーク更新

```
1. 変更内容を聞く
2. git checkout -b docs/<description> または hotfix/<description>
3. フレームワークファイルを更新
4. コミットしてPR作成を案内
```

### コミットメッセージ規約

```
<type>(<scope>): <description>

type:
  feat     — 新機能・新成果物
  fix      — バグ修正
  docs     — ドキュメント更新
  review   — レビュー結果
  test     — テスト追加・修正
  refactor — リファクタリング
  chore    — 雑務（CI/CD更新等）

scope:
  プロジェクト名またはフレームワーク要素名

例:
  feat(my-app): 要求仕様書を作成
  review(my-app): 方式設計レビュー結果
  docs(maestro): テンプレートにCSV変換手順を追加
```
