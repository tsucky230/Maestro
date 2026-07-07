# チャット生ログ（Raw Transcript）

> **テンプレート使用方法**: 本ファイルをコピーし、用途に応じて以下へ配置する。
>
> - フレームワーク更新（main相当）: `LOG/YYYY-MM-DD_NNN_FRAMEWORK_<概要>.md`
> - プロジェクト作業: `docs/projects/<project>/logs/raw-chat/YYYY-MM-DD_NNN_<工程>_<概要>.md`
>
> このログは、`conversation-log.md` のような構造化サマリーではなく、**人間↔エージェントの発話を時系列で近い形で残すための任意ログ**。

---

## メタデータ

| 項目 | 内容 |
|------|------|
| 収集開始 | YYYY-MM-DD HH:MM |
| 収集終了 | YYYY-MM-DD HH:MM |
| 記録モード | FRAMEWORK / PROJECT |
| プロジェクト名 | （PROJECT時のみ） |
| 工程 | SWP1 / SWP2 / ... / REV / GEN |
| エージェント | Copilot / Claude / Codex / Antigravity |
| モデル | （例: GPT-5.3-Codex） |
| トークン計測方式 | 実測（API usage） / 推定（文字数換算） |
| 入力トークン | 0 |
| 出力トークン | 0 |
| 合計トークン | 0 |
| 保存方針 | gitignore対象 / Git管理対象 |

> **必須**: 生ログを保存する際は、`収集開始` / `収集終了` / `モデル` / `合計トークン` を必ず埋めること。
> 実測値が取得できない環境では、`docs/templates/token-usage-metrics.md` の推定ルールで記録する。

---

## Transcript

### [HH:MM:SS] USER
（ユーザー入力を記録）

### [HH:MM:SS] AGENT
（エージェント応答を記録）

### [HH:MM:SS] USER
（繰り返し）

---

## 追記メモ（任意）

- 重要な意思決定の要約
- 後で `conversation-log.md` 側に反映する事項
- セキュリティ/個人情報観点でマスクした箇所

---

## 取り扱い注意

- 生ログには機密情報が含まれる可能性があるため、公開リポジトリへは原則コミットしない。
- フレームワーク更新時（main相当）は `LOG/` を `.gitignore` 対象にする。
- プロジェクト作業時は `.gitignore` へ追加するかを人間に確認して選択する。
- トークン値は「課金値（実測）」と「推定値」を混在させない。推定の場合はメタデータに明記する。
