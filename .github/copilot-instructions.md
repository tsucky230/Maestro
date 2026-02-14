# Maestro — GitHub Copilot Custom Instructions

> This file configures GitHub Copilot behavior for the Maestro project.
> Copilotはこのファイルを自動読み込みし、すべてのChat/Agentセッションに適用します。

## 必読

**作業開始前に必ず `AGENTS.md`（プロジェクトルート）を読み込んでください。**
プロセス規約・トレーサビリティルール・テンプレート参照方法が記載されています。

## 起動時の必須アクション（`agents/branch-and-onboarding.md` §20）

1. **まずインタラクティブメニューを提示する**（新規開発 / 継続 / レビュー / 整合性チェック等）
2. **プロジェクト作業の場合は必ず作業用ブランチを作成してから開始する**
3. `main` ブランチで直接プロジェクト成果物をコミットしてはならない

## 品質ルール（`agents/review-and-quality.md`, `agents/formal-design.md` 等）

1. **成果物提出前に自己評価を実行する**（`knowledge/self-evaluation.md` 参照）
2. **各工程完了時にメトリクスを計測し品質ゲートを通過する**（`agents/review-and-quality.md` §21）
3. **方式設計ではFMEAを実施する**（`agents/formal-design.md` §24）
4. **レビューではウォークスルー/インスペクション技法を選択する**（`agents/review-and-quality.md` §26）
5. **ファイル変更時は `dependency-map.md` で影響先を特定し整合性チェックする**（`agents/consistency-and-change.md` §28）

## Copilot固有ルール

### コード補完時

- 新しい関数・クラスを生成する際は、Docstringに `@trace DET-XXX` を含める
- テストコード生成時は `@trace UT-XXX` / `IT-XXX` / `QT-XXX` を含める
- コメントには関連する設計書タグへの参照を記述する

### Chat・Agent利用時

- 要求ヒアリングの場合: `docs/templates/requirements-spec.md` テンプレートを使用してUSDM形式で記述する
- 設計の場合: `docs/templates/` 配下の対応テンプレートを使用する
- レビューの場合: `knowledge/` 配下の観点表・チェックリストを参照する
- **対話ログを記録する**（`docs/templates/conversation-log.md` テンプレート使用, `agents/sub-agent-and-context.md` §19）

### コミットメッセージ

```
<type>(<scope>): <description>

traces-to: タグ一覧

type: feat / fix / docs / review / test / refactor / chore
scope: プロジェクト名 または フレームワーク要素名
```

例:

```
feat(my-app): ユーザー認証モジュールの詳細設計を実装

traces-to: DET-001, DET-002
```

## トレーサビリティタグ体系

```
REQ-XXX → SPEC-XXX → ARC-XXX → DET-XXX → SRC-XXX / UT-XXX
                                         → IT-XXX
                    → QT-XXX
```

詳細は `agents/process-and-traceability.md` §3 を参照。

## テンプレート・知見の場所

- `docs/templates/` — 各工程テンプレート（整合性レビュー、対話ログ含む）
- `knowledge/` — レビュー観点表、トラブル事例、チェックリスト
- `.github/workflows/security.yml` — セキュリティCI/CD（SBOM/脆弱性/スニペット検出）
