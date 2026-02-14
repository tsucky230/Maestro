# OSS管理・コンプライアンス

> このファイルは `AGENTS.md` Section 15, 18 の内容を含みます。

---

## 15. OSS管理・SBOM・脆弱性管理（EU CRA準拠）

> **適用規格**: EU Cyber Resilience Act (Regulation 2024/2847)
> 2027年12月11日までにすべてのデジタル製品で準拠が必要。

### OSS選定ルール

1. **致命的な脆弱性（Critical/High）が未修正のOSSは使用禁止**
2. 選定時に以下を **すべて** 確認する:

| 確認項目 | 基準 | NOASSERTION不可 |
|---------|------|----------------|
| コンポーネント名 | 正式名称を記録 | ✅ |
| バージョン | 使用している正確なバージョン | ✅ |
| サプライヤー（開発元） | 組織名または個人名 | ✅ |
| ライセンス | SPDX License Identifier で記録（例: `MIT`, `Apache-2.0`） | ✅ |
| 入手先URL | パッケージレジストリまたはリポジトリのURL | ✅ |
| 既知の脆弱性 | CVE/NVDで Critical/High が未修正でないこと | — |
| メンテナンス状況 | 直近1年以内にリリースがあること | — |
| コミュニティ | GitHub Stars 100以上 または 信頼できる組織が管理 | — |
| ライセンス互換性 | プロジェクトのライセンスと互換性があること | — |

### SBOM出力形式（3形式必須）

すべてのSBOMは以下の **3形式** で出力する:

| 形式 | フォーマット | 用途 | ツール |
|------|-----------|------|--------|
| **SPDX 3.0** | JSON (`.spdx.json`) | 規制当局への提出、国際標準準拠 | Microsoft SBOM Tool / spdx-tools |
| **CycloneDX 1.6** | JSON (`.cdx.json`) | 脆弱性管理ツール連携、VEX対応 | Syft / CycloneDX CLI |
| **CSV** | CSV (`.csv`) | 人間による確認・レビュー | JSON → CSV 変換スクリプト |

### SBOM CSV項目（人間可読形式）

CSV形式のSBOMには以下の項目を必ず含める:

```csv
コンポーネント名,バージョン,ライセンス,サプライヤー,入手先URL,パッケージ種別,直接/間接依存,ハッシュ(SHA-256)
requests,2.31.0,Apache-2.0,Kenneth Reitz / PSF,https://pypi.org/project/requests/,pypi,direct,a1b2c3d4...
```

| CSV項目 | 説明 | NOASSERTION許容 |
|---------|------|:---:|
| コンポーネント名 | パッケージ正式名 | ❌ |
| バージョン | 使用バージョン（セマンティックバージョニング） | ❌ |
| ライセンス | SPDX License Identifier | ❌ |
| サプライヤー | 開発組織名/個人名 | ❌ |
| 入手先URL | レジストリURL / リポジトリURL | ❌ |
| パッケージ種別 | pypi / npm / maven / go / crate 等 | ❌ |
| 直接/間接依存 | direct（直接） / transitive（間接） | ❌ |
| ハッシュ(SHA-256) | パッケージの完全性検証用 | ❌ |

### NOASSERTION排除プロセス

**SBOMにおいて `NOASSERTION`（情報不明）は原則として許容しない。** 以下の多段階プロセスで情報を確定させる:

```
Step 1: lockファイル解析
  └─ バージョン、直接/間接依存の特定
  
Step 2: パッケージレジストリAPI照会
  ├─ PyPI API: https://pypi.org/pypi/{name}/{version}/json
  ├─ npm Registry: https://registry.npmjs.org/{name}/{version}
  ├─ Maven Central: https://search.maven.org/solrsearch/select?q=...
  ├─ pkg.go.dev: https://pkg.go.dev/{module}@{version}
  └─ crates.io: https://crates.io/api/v1/crates/{name}/{version}
  └─ ライセンス、サプライヤー、入手先URLを取得

Step 3: リポジトリ直接調査（Step 2で不足がある場合）
  ├─ LICENSE / COPYING ファイルの確認
  ├─ package.json / setup.py / Cargo.toml 等のメタデータ確認
  └─ README / NOTICE ファイルの著作権表示確認

Step 4: 手動確認（Step 3でも不足がある場合）
  ├─ プロジェクトWebサイトでのライセンス表示確認
  ├─ メーリングリスト / Issue Tracker での公式見解確認
  └─ 見つからない場合は「REVIEW-REQUIRED」として記録し、人間の確認を要求
```

### 脆弱性レポート出力形式

脆弱性スキャン結果は **JSON** と **CSV** の両形式で出力する:

#### JSON形式（ツール連携用）

```json
{
  "scan_date": "2025-01-15T09:00:00Z",
  "tool": "trivy",
  "total_vulnerabilities": 3,
  "vulnerabilities": [
    {
      "id": "CVE-2024-XXXXX",
      "severity": "HIGH",
      "component": "package-name",
      "version": "1.2.3",
      "fixed_version": "1.2.4",
      "description": "...",
      "reference": "https://nvd.nist.gov/vuln/detail/CVE-2024-XXXXX"
    }
  ]
}
```

#### CSV形式（人間確認用）

```csv
CVE-ID,深刻度,コンポーネント,現バージョン,修正バージョン,説明,参照URL,対応状況
CVE-2024-XXXXX,HIGH,package-name,1.2.3,1.2.4,説明文,https://nvd.nist.gov/...,未対応
```

### SBOM品質検証ルール

CI/CDパイプラインで以下の品質チェックを自動実行する:

| チェック項目 | 条件 | 違反時のアクション |
|------------|------|:---:|
| NOASSERTION検出 | ライセンス/サプライヤー/入手先が NOASSERTION | ❌ ビルド失敗 |
| ライセンス互換性 | Copyleft系ライセンスの混入 | ⚠️ 警告 |
| 脆弱性（Critical） | CVSS 9.0以上 | ❌ ビルド失敗 |
| 脆弱性（High） | CVSS 7.0以上 | ⚠️ 警告 |
| ハッシュ不一致 | 配布パッケージの改ざん疑い | ❌ ビルド失敗 |

### SBOM生成ツール（言語別）

| 言語 | lockファイル | CycloneDX 1.6 | SPDX 3.0 |
|------|------------|---------------|----------|
| Python | `requirements.txt` / `poetry.lock` | Syft / `cyclonedx-py` | Microsoft SBOM Tool |
| JavaScript/TS | `package-lock.json` / `yarn.lock` | Syft / `cyclonedx-npm` | Microsoft SBOM Tool |
| Java | `pom.xml` / `build.gradle.lock` | Syft / `cyclonedx-maven` | Microsoft SBOM Tool |
| Go | `go.sum` | Syft / `cyclonedx-gomod` | Microsoft SBOM Tool |
| Rust | `Cargo.lock` | Syft / `cyclonedx-rust-cargo` | Microsoft SBOM Tool |

### CI/CDでの自動チェック

- `.github/workflows/security.yml` — GitHub Actions用セキュリティパイプライン
- `.gitlab-ci-security.yml` — GitLab CI用セキュリティパイプライン
- 詳細は各ファイルを参照

### ThirdPartyLicense（EU CRA準拠）

使用するすべてのOSSのライセンス情報を `THIRD_PARTY_LICENSES` ファイルに集約する。以下を必ず含める:

| 必須項目 | 説明 |
|---------|------|
| コンポーネント名 | 正式名称 |
| バージョン | 使用バージョン |
| ライセンス | SPDX License Identifier |
| サプライヤー | 開発組織名/個人名 |
| 入手先URL | パッケージレジストリ/リポジトリURL |
| ライセンス本文 | ライセンス条文全文またはURL |

---

## 18. OSSスニペット検出

### 目的

開発者（人間・AI双方）が**無意識にOSSのコードをコピーして使用**し、ライセンス違反を犯すリスクを防止する。特にAIコーディングアシスタントが生成するコードには、学習データに含まれるOSSコードの断片が混入する可能性がある。

### スキャン対象

| 対象 | 説明 |
|------|------|
| `src/` 配下の全ソースコード | プロダクションコード |
| `tests/` 配下の全テストコード | テストコード |
| 設定ファイル | Dockerfile、CI/CD設定等 |

### 検出ツール

| ツール | 用途 | ライセンス |
|--------|------|-----------|
| **ScanCode Toolkit** | ライセンス・著作権・スニペット検出 | Apache-2.0 |
| **FOSSology** (オプション) | 大規模プロジェクト向けWebベース分析 | GPL-2.0 |

### ScanCode実行コマンド

```bash
# フルスキャン（ライセンス + 著作権 + スニペット検出）
scancode \
  --license --copyright --info --package \
  --license-text --license-text-diagnostics \
  --classify \
  --json-pp oss-snippet-report.json \
  --csv oss-snippet-report.csv \
  --processes 4 \
  src/

# 結果の概要表示
scancode --license --copyright --summary \
  --json-pp oss-summary.json \
  src/
```

### 検出結果の評価基準

| スコア | 判定 | 対応 |
|--------|------|------|
| ライセンス一致 95%以上 | 🔴 **高リスク**: ほぼ完全なコピー | 即時対応必須。ライセンス遵守 or コード置換 |
| ライセンス一致 70-94% | 🟡 **要確認**: 部分的な類似 | ライセンス確認、必要に応じて帰属表示 |
| ライセンス一致 50-69% | 🟢 **低リスク**: 偶発的類似の可能性 | 記録のみ |
| ライセンス一致 50%未満 | ⚪ **問題なし** | — |

### スニペット検出時の対応フロー

```
1. ScanCodeでスニペット検出
   │
2. ライセンスを確認
   ├─ Permissive (MIT, BSD, Apache等)
   │   └─ 帰属表示を THIRD_PARTY_LICENSES に追加
   │      └─ ソースコードのコメントにライセンス表示を追加
   │
   ├─ Copyleft (GPL, LGPL, AGPL等)
   │   └─ 🔴 プロジェクトのライセンスと互換性を確認
   │      ├─ 互換性あり → 帰属表示を追加
   │      └─ 互換性なし → コードを代替実装に置き換え
   │
   └─ ライセンス不明
       └─ 🟡 原著作者に確認 or コードを代替実装に置き換え
```

### レポート出力形式

#### JSON形式（ツール連携用）

ScanCodeのデフォルト出力（`--json-pp`）を使用。

#### CSV形式（人間確認用）

```csv
ファイルパス,行範囲,検出ライセンス,一致度(%),OSSコンポーネント,OSSリポジトリURL,リスクレベル,対応状況
src/utils/parser.py,45-78,MIT,87.5,beautiful-soup4,https://github.com/...,要確認,未対応
```

### CI/CDでの自動スキャン

- `.github/workflows/security.yml` の `oss-snippet-scan` ジョブで自動実行
- `.gitlab-ci-security.yml` の `oss-snippet-scan` ジョブで自動実行
- PRごとにスキャンし、高リスク検出時はマージをブロック
