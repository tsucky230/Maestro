# Maestro フレームワーク依存関係マップ

> **目的**: ファイルが変更されたとき、影響を受ける他のファイルを即座に特定する。
> 全ファイルを再読込せず、このマップで影響範囲だけをピンポイントでチェックする。
>
> **更新ルール**: フレームワークファイルを追加・削除・構造変更した場合はこのマップも更新する。

---

## 依存関係テーブル

「変更元」を変更したら、「影響先」の該当セクションとの整合性をチェックする。

### AGENTS.md（中核ファイル）

| 変更元セクション | 影響先ファイル | 影響先の確認ポイント |
|---|---|---|
| Section 1-8（プロセス基盤） | `develop.md` Step 1-7 | ワークフローのステップがプロセスと一致するか |
| Section 1-8 | `knowledge/checklists.md` | チェック項目がプロセスと一致するか |
| Section 1-8 | `manual.md` ユースケース3 | ゼロから作る手順の説明が正しいか |
| Section 3（トレーサビリティ） | `docs/templates/traceability-matrix.md` | タグ体系が一致するか |
| Section 3 | `manual.md` ユースケース5 | トレーサビリティの説明が正しいか |
| Section 9（サブエージェント） | `develop.md` 事前準備 | コンテキストファイルの扱いが一致するか |
| Section 10（Mermaid） | `docs/templates/architecture-design.md` | 図の種類・命名規約が一致するか |
| Section 10 | `docs/templates/detailed-design.md` | クラス図の規約が一致するか |
| Section 11（TDD） | `develop.md` Step 4 | TDD手順との一致 |
| Section 12（コード品質） | `knowledge/review-perspectives.md` §5 | コードレビュー観点との一致 |
| Section 13（セキュリティ） | `knowledge/review-perspectives.md` §5.4 | セキュリティチェックとの一致 |
| Section 13 | `.github/workflows/security.yml` | CI/CDのセキュリティチェックとの一致 |
| Section 14（テストダブル） | `develop.md` Step 4 | テストダブル手順との一致 |
| Section 15（SBOM/CRA） | `.github/workflows/security.yml` | SBOMツール・フォーマットの一致 |
| Section 15 | `.gitlab-ci-security.yml` | 同上（GitLab版） |
| Section 15 | `THIRD_PARTY_LICENSES` | ライセンス管理方針の一致 |
| Section 17（整合性レビュー） | `docs/templates/consistency-review.md` | テンプレートの観点がルールと一致するか |
| Section 17 | `knowledge/review-perspectives.md` §7 | 整合性レビュー観点との一致 |
| Section 17 | `develop.md` Step 8 | ワークフローの手順との一致 |
| Section 18（OSSスニペット） | `.github/workflows/security.yml` | スキャンツール・閾値の一致 |
| Section 18 | `.gitlab-ci-security.yml` | 同上（GitLab版） |
| Section 19（対話ログ） | `docs/templates/conversation-log.md` | テンプレートの構造との一致 |
| Section 19 | `develop.md` 対話ログルール | ワークフローのログ手順との一致 |
| Section 19 | `knowledge/checklists.md` 対話ログ | チェック項目との一致 |
| Section 20（ブランチ/メニュー） | `develop.md` Step 0 | メニュー内容・ブランチ命名の一致 |
| Section 20 | `CLAUDE.md` 起動時アクション | 起動ルールの一致 |
| Section 20 | `copilot-instructions.md` 起動時アクション | 起動ルールの一致 |
| Section 20 | `README.md` ブランチ戦略 | ブランチ図・説明の一致 |
| Section 20 | `manual.md` ブランチルール | ブランチの説明の一致 |
| Section 21（メトリクス） | `knowledge/quality-metrics.md` | メトリクス定義・閾値の一致 |
| Section 21 | `knowledge/self-evaluation.md` | 自己評価のメトリクス参照の一致 |
| Section 21 | `develop.md` 品質ゲートルール | ゲート手順の一致 |
| Section 21 | `knowledge/checklists.md` 品質ゲート | チェック項目の一致 |
| Section 22（アーキテクチャ適合度） | `docs/templates/architecture-design.md` | ADR記述方式の一致 |
| Section 23（形式的仕様） | `docs/templates/detailed-design.md` | 契約記述フォーマットの一致 |
| Section 23 | `knowledge/review-perspectives.md` §9 | 形式仕様レビュー観点の一致 |
| Section 24（FMEA/FTA） | `docs/templates/fmea-fta.md` | テンプレートの評価尺度・RPN基準の一致 |
| Section 24 | `knowledge/checklists.md` FMEA | チェック項目の一致 |
| Section 24 | `knowledge/review-perspectives.md` §10 | FMEAレビュー観点の一致 |
| Section 24 | `develop.md` FMEAルール | ワークフローの適用タイミングの一致 |
| Section 25（自己評価） | `knowledge/self-evaluation.md` | チェック項目・フローの一致 |
| Section 25 | `develop.md` 品質ゲートルール | 自己評価手順の一致 |
| Section 25 | `knowledge/checklists.md` 自己評価 | チェック項目の一致 |
| Section 26（レビュープロトコル） | `knowledge/review-perspectives.md` §11 | レビュー技法・分類の一致 |
| Section 26 | `develop.md` レビュー依頼 | レビュー手順の一致 |
| Section 27（マルチプロジェクト学習） | `docs/templates/retrospective.md` | テンプレートの構造の一致 |
| Section 27 | `knowledge/patterns.md` | パターン記述方式の一致 |
| Section 27 | `develop.md` Step 9 | レトロスペクティブ手順の一致 |
| Section 27 | `knowledge/checklists.md` レトロ | チェック項目の一致 |

### プラットフォーム設定ファイル間の整合性

| 変更元 | 影響先 | 確認ポイント |
|---|---|---|
| `CLAUDE.md` | `copilot-instructions.md` | 起動ルール・品質ルールが同等か |
| `copilot-instructions.md` | `CLAUDE.md` | 同上（逆方向） |
| `develop.md` | `CLAUDE.md` / `copilot-instructions.md` | ワークフロー変更がプラットフォーム設定に反映されているか |
| `README.md` | `AGENTS.md` Section 20 | セクション一覧・機能説明の一致 |
| `manual.md` | `AGENTS.md` 全体 | マニュアルの説明がルールと一致しているか |

### テンプレート ↔ ナレッジの整合性

| 変更元 | 影響先 | 確認ポイント |
|---|---|---|
| `docs/templates/*` （テンプレート群） | `knowledge/checklists.md` | テンプレート構造の変更がチェック項目に反映されているか |
| `knowledge/review-perspectives.md` | `AGENTS.md` 該当Section | レビュー観点の追加がルールに反映されているか |
| `knowledge/quality-metrics.md` | `AGENTS.md` Section 21 | メトリクス閾値の変更がルールに反映されているか |
| `knowledge/self-evaluation.md` | `AGENTS.md` Section 25 | 自己評価項目の変更がルールに反映されているか |

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
| YYYY-MM-DD | AGENTS.md §21 | quality-metrics.md | 閾値一致 | ✅ |
| YYYY-MM-DD | AGENTS.md §21 | self-evaluation.md | メトリクス参照 | ✅ |
```
