# CLAUDE.md — Maestro Project Configuration for Claude Code

> このファイルはClaude Codeがプロジェクトコンテキストとして読み込む設定ファイルです。

## プロジェクト: Maestro

ESPR 2.0準拠のソフトウェア開発エージェントフレームワーク。

## 必読ファイル

**作業開始前に必ず `AGENTS.md` を読み込んでください。** そこにプロセス規約・トレーサビリティルール・テンプレート参照方法がすべて記載されています。

## 起動時の必須アクション（AGENTS.md Section 20）

1. **まずインタラクティブメニューを提示する**（新規開発 / 継続 / レビュー / 整合性チェック等）
2. **プロジェクト作業の場合は必ず作業用ブランチを作成してから開始する**
3. `main` ブランチで直接プロジェクト成果物をコミットしてはならない

## 品質ルール（AGENTS.md Section 21-27）

1. **成果物提出前に自己評価を実行する**（`knowledge/self-evaluation.md` 参照）
2. **各工程完了時にメトリクスを計測し品質ゲートを通過すること**（Section 21）
3. **方式設計ではFMEAを実施する**（RPN≥100はFTAも実施, Section 24）
4. **詳細設計では前提/事後条件を記述する**（Design by Contract, Section 23）
5. **レビューではプロトコルに従いウォークスルー/インスペクションを選択する**（Section 26）
6. **プロジェクト完了時にレトロスペクティブを実施する**（Section 27）

## Claude Code固有の指示

### 対話スタイル

- 要求ヒアリング時は**段階的に深掘り**する（一度に多くの質問をしない）
- ユーザーが曖昧な要求を述べた場合は、具体例を示して確認する
- リスクや懸念事項を見つけたら、**先に共有してから**先に進む

### サブエージェント委譲（AGENTS.md Section 9）

- 工程を跨ぐ際は必ず `docs/projects/<project>/context/` のコンテキストファイルを更新する
- サブエージェントに委譲する際は AGENTS.md Section 9 の委譲指示テンプレートを使用する

### 拡張思考の活用

- 要求仕様の作成時: 全体像を把握してから個別仕様に落とし込む
- 設計レビュー時: 考慮漏れがないか網羅的にチェックする
- テスト設計時: 正常系・異常系・境界値を体系的に洗い出す

### 成果物生成時の注意

1. 必ず `AGENTS.md` Section 3 の**トレーサビリティ規約**に従ってタグを付与する
2. 成果物作成後、`knowledge/` 配下の観点表・チェックリストでセルフチェックを行う
3. 前工程の成果物がある場合は必ず読み込み、整合性を確認する
4. **設計書にはMermaid図を必ず含める**（AGENTS.md Section 10参照）
5. **詳細設計ではソフトウェアの意図を日本語で詳しく書く**

### TDDワークフロー（AGENTS.md Section 11）

1. 詳細設計書をインプットに**テストを先に書く**（RED）
2. テストが失敗することを確認する
3. テストを満たす最小限のコードを書く（GREEN）
4. コード品質規約を適用してリファクタリング（REFACTOR）

### コーディング時の注意

- 関数・クラスのDocstringに `@trace DET-XXX` タグを含める
- テスト関数のDocstringに `@trace UT-XXX` / `IT-XXX` / `QT-XXX` タグを含める
- トレーサビリティマトリクスの更新を忘れないこと
- **関数は100行以内、サイクロマティック複雑度50以内**（AGENTS.md Section 12）
- **セキュリティコーディング規約に従う**（AGENTS.md Section 13）
- **テストダブル（Mock/Stub/Driver）を適切に使用する**（AGENTS.md Section 14）
- **OSS選定時は致命的な脆弱性がないか確認する**（AGENTS.md Section 15, EU CRA準拠）

### 対話ログの記録（AGENTS.md Section 19）

- **すべての工程開始時に対話ログを作成する**（`docs/templates/conversation-log.md` テンプレート使用）
- ファイル名: `YYYY-MM-DD_NNN_<工程コード>_<概要>.md`（例: `2025-02-14_001_SWP1_要求ヒアリング.md`）
- 決定事項は「決定事項」セクションに明記する（本文中に埋もれさせない）
- 対話終了時に `conversation-index.md` を更新する
- 対話の知見は `knowledge/trouble-cases.md` に反映する

### 整合性レビュー（AGENTS.md Section 17）

- 企画書↔仕様書など上流↔下流文書間の矛盾・不整合を検出する
- `docs/templates/consistency-review.md` テンプレートを使用してレポートを作成する
- チェック観点: 用語統一、数値整合、スコープ一致、非機能要求反映、制約継承

### OSSスニペット検出（AGENTS.md Section 18）

- ソースコードにOSSのコードが無断で混入していないかScanCodeでスキャンする
- 高リスク検出（95%以上）は即時対応必須

## テンプレートの場所

- `docs/templates/` — 各工程のテンプレート（整合性レビュー、対話ログ含む）
- `knowledge/` — レビュー観点表、トラブル事例、チェックリスト
- `.github/workflows/security.yml` — セキュリティCI/CD（SBOM/脆弱性/スニペット検出）
- `.gitlab-ci-security.yml` — GitLab CIセキュリティ
- `THIRD_PARTY_LICENSES` — OSSライセンス一覧（CRA準拠）
