# 変更履歴 / Changelog

このファイルはMaestroフレームワークの変更履歴を記録します。

---

## [Unreleased]

### 2025-02-15

- feat(maestro): 組み込みシステム開発知見を統合 — `knowledge/embedded-constraints.md` 新規作成、各工程エージェント・チェックリスト・レビュー観点に組み込み固有ステップ追加
- refactor(maestro): AGENTS.md をモジュール化 — コア索引 + agents/ 配下10モジュールに分割

### 2025-02-14

- docs(maestro): 利用マニュアル（manual.md）を新規作成 — 7つのユースケースで初心者向け解説
- feat(maestro): 変更管理・差分整合性チェックを追加（AGENTS.md Section 28, dependency-map.md）

- feat(maestro): メトリクス駆動 品質ゲートを追加（AGENTS.md Section 21, knowledge/quality-metrics.md）
- feat(maestro): アーキテクチャ適合度テストを追加（AGENTS.md Section 22）
- feat(maestro): 形式的仕様記述（軽量版）を追加（AGENTS.md Section 23）
- feat(maestro): FMEA/FTA統合を追加（AGENTS.md Section 24, docs/templates/fmea-fta.md）
- feat(maestro): エージェント自己評価メカニズムを追加（AGENTS.md Section 25, knowledge/self-evaluation.md）
- feat(maestro): レビュープロトコルを追加（AGENTS.md Section 26, review-perspectives.md更新）
- feat(maestro): マルチプロジェクト学習を追加（AGENTS.md Section 27, knowledge/patterns.md, docs/templates/retrospective.md）
- docs(maestro): ワークフロー・チェックリスト・README・CLAUDE.md・copilot-instructions.md を全面更新
- feat(maestro): CHANGELOG.md 作成、変更履歴・コミットルールをワークフローに追加
- feat(maestro): ブランチ戦略・起動時インタラクティブメニューを追加（AGENTS.md Section 20）
- feat(maestro): 会話ログ機能を追加（AGENTS.md Section 19, テンプレート, ワークフロー統合）
- feat(maestro): OSSスニペット検出を追加（AGENTS.md Section 18, ScanCode CI/CD統合）
- feat(maestro): 成果物間 整合性レビュー機能を追加（AGENTS.md Section 17, テンプレート）
- feat(maestro): EU CRA準拠SBOM強化 — SPDX 3.0 + CycloneDX 1.6 + CSV出力（AGENTS.md Section 15 全面改訂）
- feat(maestro): 脆弱性レポートCSV出力、NOASSERTION排除プロセスを追加
- feat(maestro): CI/CDパイプライン完全書き換え（GitHub Actions + GitLab CI）
- feat(maestro): テストダブル規約を追加（AGENTS.md Section 14）
- feat(maestro): セキュリティコーディング規約を追加（AGENTS.md Section 13）
- feat(maestro): コード品質規約を追加（AGENTS.md Section 12）
- feat(maestro): TDDワークフローを追加（AGENTS.md Section 11）
- feat(maestro): Mermaid UML設計図規約を追加（AGENTS.md Section 10）
- feat(maestro): サブエージェント委譲・コンテキスト継続を追加（AGENTS.md Section 9）
- feat(maestro): 初期フレームワーク構築 — ESPR 2.0プロセス基盤（Section 1-8）
- docs(maestro): README.md にブランチ戦略・メニュー・セクション一覧を追加
- docs(maestro): CLAUDE.md / copilot-instructions.md を全セクション対応に更新
- chore(maestro): .github/workflows/security.yml 作成
- chore(maestro): .gitlab-ci-security.yml 作成
- chore(maestro): THIRD_PARTY_LICENSES テンプレート作成
