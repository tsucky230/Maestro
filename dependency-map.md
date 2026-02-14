# Maestro フレームワーク依存関係マップ

> **目的**: ファイルが変更されたとき、影響を受ける他のファイルを即座に特定する。
> 全ファイルを再読込せず、このマップで影響範囲だけをピンポイントでチェックする。
>
> **更新ルール**: フレームワークファイルを追加・削除・構造変更した場合はこのマップも更新する。

---

## 依存関係テーブル

「変更元」を変更したら、「影響先」の該当セクションとの整合性をチェックする。

### AGENTS.md（コア索引ファイル）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| コア（プロジェクト概要・ロードマップ） | `develop.md` Step 0 | ワークフロー起動手順の一致 |
| コア（ディレクトリ構成 §7,16） | `manual.md` ディレクトリ説明 | ディレクトリ構成の説明が正しいか |
| コア（モジュール索引テーブル §2） | `agents/*.md` | モジュール一覧とファイル名の一致 |

### agents/process-and-traceability.md（§2,3,4,6,8）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §2（プロセスフロー） | `develop.md` Step 1-7 | ワークフローのステップがプロセスと一致するか |
| §2 | `knowledge/checklists.md` | チェック項目がプロセスと一致するか |
| §2 | `manual.md` ユースケース3 | ゼロから作る手順の説明が正しいか |
| §3（トレーサビリティ） | `docs/templates/traceability-matrix.md` | タグ体系が一致するか |
| §3 | `manual.md` ユースケース5 | トレーサビリティの説明が正しいか |

### agents/review-and-quality.md（§5,21,25,26）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §21（メトリクス） | `knowledge/quality-metrics.md` | メトリクス定義・閾値の一致 |
| §21 | `knowledge/self-evaluation.md` | 自己評価のメトリクス参照の一致 |
| §21 | `develop.md` 品質ゲートルール | ゲート手順の一致 |
| §21 | `knowledge/checklists.md` 品質ゲート | チェック項目の一致 |
| §25（自己評価） | `knowledge/self-evaluation.md` | チェック項目・フローの一致 |
| §25 | `develop.md` 品質ゲートルール | 自己評価手順の一致 |
| §25 | `knowledge/checklists.md` 自己評価 | チェック項目の一致 |
| §26（レビュープロトコル） | `knowledge/review-perspectives.md` §11 | レビュー技法・分類の一致 |
| §26 | `develop.md` レビュー依頼 | レビュー手順の一致 |

### agents/sub-agent-and-context.md（§9,19）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §9（サブエージェント） | `develop.md` 事前準備 | コンテキストファイルの扱いが一致するか |
| §19（対話ログ） | `docs/templates/conversation-log.md` | テンプレートの構造との一致 |
| §19 | `develop.md` 対話ログルール | ワークフローのログ手順との一致 |
| §19 | `knowledge/checklists.md` 対話ログ | チェック項目との一致 |

### agents/mermaid-uml.md（§10）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §10（Mermaid） | `docs/templates/architecture-design.md` | 図の種類・命名規約が一致するか |
| §10 | `docs/templates/detailed-design.md` | クラス図の規約が一致するか |

### agents/coding-standards.md（§11,12,13,14）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §11（TDD） | `develop.md` Step 4 | TDD手順との一致 |
| §12（コード品質） | `knowledge/review-perspectives.md` §5 | コードレビュー観点との一致 |
| §13（セキュリティ） | `knowledge/review-perspectives.md` §5.4 | セキュリティチェックとの一致 |
| §13 | `.github/workflows/security.yml` | CI/CDのセキュリティチェックとの一致 |
| §14（テストダブル） | `develop.md` Step 4 | テストダブル手順との一致 |

### agents/oss-and-compliance.md（§15,18）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §15（SBOM/CRA） | `.github/workflows/security.yml` | SBOMツール・フォーマットの一致 |
| §15 | `.gitlab-ci-security.yml` | 同上（GitLab版） |
| §15 | `THIRD_PARTY_LICENSES` | ライセンス管理方針の一致 |
| §18（OSSスニペット） | `.github/workflows/security.yml` | スキャンツール・閾値の一致 |
| §18 | `.gitlab-ci-security.yml` | 同上（GitLab版） |

### agents/consistency-and-change.md（§17,28）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §17（整合性レビュー） | `docs/templates/consistency-review.md` | テンプレートの観点がルールと一致するか |
| §17 | `knowledge/review-perspectives.md` §7 | 整合性レビュー観点との一致 |
| §17 | `develop.md` Step 8 | ワークフローの手順との一致 |
| §28（変更管理） | この `dependency-map.md` 自体 | 変更管理手順の一致 |

### agents/branch-and-onboarding.md（§20）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §20（ブランチ/メニュー） | `develop.md` Step 0 | メニュー内容・ブランチ命名の一致 |
| §20 | `CLAUDE.md` 起動時アクション | 起動ルールの一致 |
| §20 | `copilot-instructions.md` 起動時アクション | 起動ルールの一致 |
| §20 | `README.md` ブランチ戦略 | ブランチ図・説明の一致 |
| §20 | `manual.md` ブランチルール | ブランチの説明の一致 |

### agents/formal-design.md（§22,23,24）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §22（アーキテクチャ適合度） | `docs/templates/architecture-design.md` | ADR記述方式の一致 |
| §23（形式的仕様） | `docs/templates/detailed-design.md` | 契約記述フォーマットの一致 |
| §23 | `knowledge/review-perspectives.md` §9 | 形式仕様レビュー観点の一致 |
| §24（FMEA/FTA） | `docs/templates/fmea-fta.md` | テンプレートの評価尺度・RPN基準の一致 |
| §24 | `knowledge/checklists.md` FMEA | チェック項目の一致 |
| §24 | `knowledge/review-perspectives.md` §10 | FMEAレビュー観点の一致 |
| §24 | `develop.md` FMEAルール | ワークフローの適用タイミングの一致 |

### agents/multi-project-learning.md（§27）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §27（マルチプロジェクト学習） | `docs/templates/retrospective.md` | テンプレートの構造の一致 |
| §27 | `knowledge/patterns.md` | パターン記述方式の一致 |
| §27 | `develop.md` Step 9 | レトロスペクティブ手順の一致 |
| §27 | `knowledge/checklists.md` レトロ | チェック項目の一致 |

### プラットフォーム設定ファイル間の整合性

| 変更元 | 影響先 | 確認ポイント |
|---|---|---|
| `CLAUDE.md` | `copilot-instructions.md` | 起動ルール・品質ルールが同等か |
| `copilot-instructions.md` | `CLAUDE.md` | 同上（逆方向） |
| `develop.md` | `CLAUDE.md` / `copilot-instructions.md` | ワークフロー変更がプラットフォーム設定に反映されているか |
| `README.md` | `AGENTS.md` コア索引 | セクション一覧・機能説明の一致 |
| `manual.md` | `AGENTS.md` + `agents/*.md` | マニュアルの説明がルールと一致しているか |

### テンプレート ↔ ナレッジの整合性

| 変更元 | 影響先 | 確認ポイント |
|---|---|---|
| `docs/templates/*` （テンプレート群） | `knowledge/checklists.md` | テンプレート構造の変更がチェック項目に反映されているか |
| `knowledge/review-perspectives.md` | `agents/review-and-quality.md` | レビュー観点の追加がルールに反映されているか |
| `knowledge/quality-metrics.md` | `agents/review-and-quality.md` §21 | メトリクス閾値の変更がルールに反映されているか |
| `knowledge/self-evaluation.md` | `agents/review-and-quality.md` §25 | 自己評価項目の変更がルールに反映されているか |

### knowledge/embedded-constraints.md（組み込みシステム制約）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| §1（HW逆質問テンプレート） | `agents/process-and-traceability.md` | 要求ヒアリングワークフローの呼び出し |
| §1 | `knowledge/checklists.md` SWP.1 組み込み | チェック項目の一致 |
| §1 | `develop.md` Step 1 | ワークフロー手順の一致 |
| §3（RTOS設計） | `develop.md` Step 2 | ワークフロー手順の一致 |
| §3 | `agents/formal-design.md` §24 | FMEA故障モードテンプレートとの一致 |
| §5（ロギング設計） | `agents/coding-standards.md` §29 | 組み込みコーディング規約との一致 |
| §6（テストフェーズ別観点） | `develop.md` Step 4a | テスト手順との一致 |
| §7（バッテリー管理） | `agents/coding-standards.md` §29 | 低電力モード規約との一致 |
| 全体 | `knowledge/review-perspectives.md` §12 | 組み込みレビュー観点との一致 |
| 全体 | `AGENTS.md` ロードマップ | 各工程での参照が正しいか |

---

## 変更時チェック手順

### 1. 変更したファイルを特定

```bash
git diff --name-only HEAD~1
```

### 2. このマップから影響先を検索

変更したファイルを「変更元」列で検索し、「影響先」を取得する。

### 3. 影響先の該当セクションだけ読み込んでチェック

**全ファイルを読まない。** 影響先の「確認ポイント」に記載された特定セクションだけを確認する。

### 4. 結果を検証ログに記録

```markdown
## 整合性検証ログ

| 検証日 | 変更ファイル | 影響先 | 確認ポイント | 結果 |
|--------|-----------|--------|-----------|------|
| YYYY-MM-DD | agents/review-and-quality.md §21 | quality-metrics.md | 閾値一致 | ✅ |
| YYYY-MM-DD | agents/review-and-quality.md §21 | self-evaluation.md | メトリクス参照 | ✅ |
```
