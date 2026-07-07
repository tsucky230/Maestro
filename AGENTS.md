# Maestro — ソフトウェア開発エージェント契約書

> **このファイルは、すべてのAIコーディングエージェント（GitHub Copilot, Claude Code, Codex, Antigravity）が従うべき共通規約です。**

---

## 1. プロジェクト概要

Maestroは、ESPR 2.0（組込みシステム開発プロセス参照）のプロセスモデルを一般ソフトウェア開発に適用し、人間とAIが協働して高品質なソフトウェアを構築するためのフレームワークです。

### あなた（AIエージェント）の役割

- 要求のヒアリングと仕様化の支援
- USDM形式での要求仕様書の作成
- トレーサビリティタグを付加した成果物の生成
- 各工程のレビュー・指摘
- 知見ライブラリを活用した品質チェック
- 人間との対話を通じた協働開発

---

## 2. モジュール索引テーブル

> **重要**: このファイル（コア）には共通規約のみを記載しています。工程別の詳細な規約は `agents/` 配下のモジュールファイルに分割されています。**必ず「工程別ロードマップ（Section 3）」に従い、作業に必要なモジュールを読み込んでください。**

| # | モジュール | ファイルパス | 含むセクション | テーマ |
|---|----------|------------|-------------|--------|
| 1 | プロセス基盤 | [`agents/process-and-traceability.md`](agents/process-and-traceability.md) | §2, §3, §4, §6, §8 | V字モデル・トレーサビリティ・USDM・作業フロー・用語集 |
| 2 | レビュー・品質 | [`agents/review-and-quality.md`](agents/review-and-quality.md) | §5, §21, §25, §26 | レビュー手順・品質ゲート・自己評価・レビュープロトコル |
| 3 | サブエージェント | [`agents/sub-agent-and-context.md`](agents/sub-agent-and-context.md) | §9, §19 | サブエージェント委譲・対話ログ |
| 4 | Mermaid/UML | [`agents/mermaid-uml.md`](agents/mermaid-uml.md) | §10 | Mermaid UML図規約 |
| 5 | コーディング規約 | [`agents/coding-standards.md`](agents/coding-standards.md) | §11-15 | TDD・コード品質・セキュリティ・テストダブル・AIドキュメント |
| 6 | OSS/コンプライアンス | [`agents/oss-and-compliance.md`](agents/oss-and-compliance.md) | §15, §18 | OSS/SBOM/CRA管理・OSSスニペット検出 |
| 7 | 整合性・変更管理 | [`agents/consistency-and-change.md`](agents/consistency-and-change.md) | §17, §28 | 成果物間整合性レビュー・変更管理 |
| 8 | ブランチ/起動 | [`agents/branch-and-onboarding.md`](agents/branch-and-onboarding.md) | §20 | ブランチ戦略・起動時オンボーディング |
| 9 | 形式的設計 | [`agents/formal-design.md`](agents/formal-design.md) | §22, §23, §24 | アーキテクチャ適合度・形式仕様・FMEA/FTA |
| 10 | マルチプロジェクト | [`agents/multi-project-learning.md`](agents/multi-project-learning.md) | §27 | マルチプロジェクト学習・レトロスペクティブ |
| 11 | 品質守護神 | [`agents/quality-guardian.md`](agents/quality-guardian.md) | | コードクローン検出・品質監視 |
| 12 | QAエンジニア | [`agents/qa-engineer.md`](agents/qa-engineer.md) | | ソフトウェア結合・総合テスト設計 (SWP.5/6) |

---

## 3. 工程別ロードマップ（必須読込ガイド）

> **ルール**: 各工程を開始する際、このロードマップに記載されたモジュールを **必ず** 読み込むこと。工程と無関係なモジュールは読み込まなくてよい。

### 起動時（全工程共通） — 必ず読む

| 読込対象 | 理由 |
|---------|------|
| このファイル (`AGENTS.md`) | 共通規約・ロードマップ |
| `agents/branch-and-onboarding.md` | 起動メニュー・ブランチ戦略 |
| `agents/sub-agent-and-context.md` | コンテキスト継続・対話ログ |

### SWP.1 要求仕様定義

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/process-and-traceability.md` | USDM形式・トレーサビリティタグ・V字モデル |
| `agents/review-and-quality.md` | 品質ゲート（曖昧語チェック等） |
| `knowledge/embedded-constraints.md` | 組み込みプロジェクト時: HW逆質問・非機能要求テンプレート |

### SWP.2 方式設計

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/process-and-traceability.md` | トレーサビリティタグの引き継ぎ |
| `agents/mermaid-uml.md` | コンポーネント図・シーケンス図の作成 |
| `agents/formal-design.md` | ADR・FMEA・アーキテクチャ適合度 |
| `agents/oss-and-compliance.md` | OSS選定・SBOM作成 |
| `knowledge/embedded-constraints.md` | 組み込みプロジェクト時: RTOS設計・マルチCPU通信チェック |

### SWP.3 詳細設計

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/process-and-traceability.md` | トレーサビリティタグの引き継ぎ |
| `agents/mermaid-uml.md` | クラス図・状態遷移図の作成 |
| `agents/formal-design.md` | 前提条件/事後条件（Design by Contract） |
| `agents/coding-standards.md` | コード品質規約の事前確認 |
| `knowledge/embedded-constraints.md` | 組み込みプロジェクト時: ロギング設計・低電力モード設計 |

### SWP.4 製造・単体テスト

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/coding-standards.md` | TDD・コード品質・セキュリティ・テストダブル |
| `agents/process-and-traceability.md` | トレーサビリティタグ（SRC/UT） |
| `knowledge/embedded-constraints.md` | 組み込みプロジェクト時: テストフェーズ別観点・型安全性 |

### SWP.5 結合テスト

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/coding-standards.md` | テストダブル規約 |
| `agents/mermaid-uml.md` | シーケンス図（テストシナリオ可視化） |
| `agents/process-and-traceability.md` | トレーサビリティタグ（IT） |

### SWP.6 適格性確認テスト

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/process-and-traceability.md` | 要求↔テストの対応確認（QT） |

### レビュー依頼時

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/review-and-quality.md` | レビュープロトコル・自己評価 |
| `agents/consistency-and-change.md` | 成果物間整合性チェック |

### 変更発生時

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/consistency-and-change.md` | 変更管理・差分整合性チェック |
| `dependency-map.md` | 影響先の特定 |

### プロジェクト完了時

| 追加読込モジュール | 理由 |
|-----------------|------|
| `agents/multi-project-learning.md` | レトロスペクティブ・知見の蓄積 |

---

## 7. ディレクトリ構成

### Maestroフレームワーク構成

```
Maestro/
├── AGENTS.md                          # 📌 コア規約（本ファイル: 索引＋共通規約）
├── agents/                            # 📁 エージェント規約モジュール
│   ├── process-and-traceability.md    # §2,3,4,6,8: プロセス・トレーサビリティ
│   ├── review-and-quality.md          # §5,21,25,26: レビュー・品質
│   ├── sub-agent-and-context.md       # §9,19: サブエージェント・対話ログ
│   ├── mermaid-uml.md                 # §10: Mermaid/UML
│   ├── coding-standards.md            # §11,12,13,14: コーディング規約
│   ├── oss-and-compliance.md          # §15,18: OSS/コンプライアンス
│   ├── consistency-and-change.md      # §17,28: 整合性・変更管理
│   ├── branch-and-onboarding.md       # §20: ブランチ/起動
│   ├── formal-design.md              # §22,23,24: 形式的設計
│   └── multi-project-learning.md      # §27: マルチプロジェクト学習
├── CLAUDE.md                          # Claude Code設定
├── .github/
│   ├── copilot-instructions.md        # GitHub Copilot設定
│   └── workflows/
│       └── security.yml               # セキュリティCI/CD
├── .gitlab-ci-security.yml            # GitLab CI セキュリティ
├── .agent/
│   └── workflows/
│       └── develop.md                 # Antigravity向けワークフロー
├── docs/
│   ├── templates/                     # 各工程テンプレート
│   │   ├── requirements-spec.md       # 要求仕様テンプレート (USDM)
│   │   ├── architecture-design.md     # 方式設計テンプレート
│   │   ├── detailed-design.md         # 詳細設計テンプレート
│   │   ├── test-design.md             # テスト設計テンプレート
│   │   ├── traceability-matrix.md     # トレーサビリティマトリクス
│   │   ├── review-report.md           # レビュー報告テンプレート
│   │   ├── consistency-review.md      # 整合性レビューテンプレート
│   │   ├── fmea-fta.md                # FMEA/FTA テンプレート
│   │   ├── chat-transcript-log.md     # チャット生ログテンプレート（任意）
│   │   └── retrospective.md           # レトロスペクティブテンプレート
│   └── projects/                      # 各プロジェクトの成果物
│       └── <project-name>/
│           ├── requirements/          # 要求仕様書
│           ├── architecture/          # 方式設計書
│           ├── detailed-design/       # 詳細設計書
│           ├── src/                   # ソースコード
│           ├── tests/                 # テストコード
│           ├── reviews/              # レビュー報告書
│           ├── sbom/                 # SBOM出力
│           ├── context/              # コンテキストファイル
│           └── logs/                 # 対話ログ
├── knowledge/                         # 知見ライブラリ
│   ├── review-perspectives.md         # レビュー観点表
│   ├── trouble-cases.md               # トラブル事例集
│   ├── checklists.md                  # 工程別チェックリスト
│   ├── quality-metrics.md             # メトリクス定義・閾値
│   ├── self-evaluation.md             # 自己評価チェック項目
│   ├── patterns.md                    # 推奨パターン集
│   └── embedded-constraints.md        # 組み込みシステム制約・チェックリスト
├── dependency-map.md                  # ファイル間依存関係マップ
├── LOG/                               # 任意: フレームワーク更新時のチャット生ログ（.gitignore対象）
├── manual.md                          # 利用マニュアル
├── CHANGELOG.md                       # 変更履歴
├── THIRD_PARTY_LICENSES               # OSSライセンス集約
└── 要求仕様.md                         # 要求仕様メモ
```

### プロジェクト成果物構成

```
docs/projects/<project-name>/
├── requirements/
│   └── requirements-spec.md           # 要求仕様書 (USDM形式)
├── architecture/
│   └── architecture-design.md         # 方式設計書
├── detailed-design/
│   └── detailed-design.md             # 詳細設計書
├── src/                               # ソースコード
├── tests/
│   ├── unit/                          # 単体テスト
│   ├── integration/                   # 結合テスト
│   └── qualification/                 # 適格性確認テスト
├── reviews/
│   ├── review-report.md               # レビュー報告書
│   └── consistency-review.md          # 整合性レビュー報告書
├── sbom/
│   ├── sbom.spdx.json                 # SPDX 3.0
│   ├── sbom.cdx.json                  # CycloneDX 1.6
│   ├── sbom.csv                       # CSV (人間可読)
│   ├── vulnerability-report.json      # 脆弱性レポート (JSON)
│   └── vulnerability-report.csv       # 脆弱性レポート (CSV)
├── context/
│   ├── project-context.md             # プロジェクトコンテキスト
│   ├── current-phase.md               # 現在の工程状態
│   ├── decisions-log.md               # 設計判断記録
│   └── handover-notes.md              # 引き継ぎメモ
├── logs/
│   ├── YYYY-MM-DD_NNN_<工程>_<概要>.md # 対話ログ
│   └── conversation-index.md          # 対話索引
├── metrics-log.md                     # メトリクスログ
├── traceability-matrix.md             # トレーサビリティマトリクス
└── fmea-fta.md                        # FMEA/FTA（該当時）
```

---

## 16. セクション間の相互参照ルール

### 参照の書き方

モジュール間で参照する場合は以下の形式を使用する:

```
→ `agents/review-and-quality.md` §21（品質ゲート）を参照
→ `agents/coding-standards.md` §13（セキュリティ）を参照
```

### ファイル変更時の整合性チェック

ファイルを変更した場合は、**必ず** `dependency-map.md` を参照して影響先を確認し、整合性をチェックすること。詳細な手順は `agents/consistency-and-change.md` §28 を参照。

---

## 29. チャット生ログ（任意機能）

> `agents/sub-agent-and-context.md` §19（対話ログ）を補完する任意機能。

1. チャット生ログは**デフォルトOFF**とする。
2. 人間が「ログを取って」等を指示した場合のみ、生ログ記録を開始する。
3. 記録形式は `docs/templates/chat-transcript-log.md` を使用する。
4. 保存先:
	- フレームワーク更新（main相当）: `LOG/`
	- プロジェクト作業: `docs/projects/<project>/logs/raw-chat/`
5. `.gitignore` 方針:
	- フレームワーク更新（main相当）は `LOG/` を `.gitignore` に含める（必須）
	- プロジェクト作業は `.gitignore` 追加可否を人間に確認して選択する（必須）
6. 生ログ保存時は、**モデル名・開始/終了時刻・トークン消費量（入力/出力/合計）** を必ず記録する。

## 30. コンテキスト検索モード（標準優先）

1. Maestroの標準運用は、**拡張機能非依存でも成立すること**を前提とする。
2. Vexp等の拡張は「任意の高速化レイヤ」として扱い、未導入・停止時も作業継続可能でなければならない。
3. 運用モードは `standard` と `auto` の2つを基本とし、専用の `vexp` 単独モードは設けない。
4. 推奨モードは `auto` とし、利用可能なら拡張を使い、利用不可なら `standard` にフォールバックする。
5. エージェントの説明・手順では、常に `standard` 手順を先に示し、拡張利用（Vexp等）は `auto` 運用の補足として提示する。
