# メトリクス定義・閾値根拠

> **使用方法**: 各工程完了時に、該当するメトリクスを計測し、閾値と比較する。
> メトリクスの計測結果は `docs/projects/<project>/context/metrics-log.md` に記録する。

---

## メトリクス閾値の根拠

### 要求あたり仕様数 ≥ 2.0

**根拠**: 1つの要求に対して最低2つの仕様（正常系仕様 + 異常系/境界仕様）がなければ、検証可能な仕様として不十分。IEEE 830の品質属性「検証可能性」に基づく。

### 曖昧語出現率 0%

**根拠**: 曖昧な仕様は複数の解釈を生み、下流工程での手戻りの主要原因。Berry et al. (2003) の研究では、曖昧語を含む仕様は含まない仕様に比べ3.2倍の欠陥を生む。

### コンポーネント結合度 ≤ 3

**根拠**: Martin (2003)「Clean Architecture」の安定依存の原則。結合度4以上のコンポーネントは変更波及の中心になりやすい。

### C1カバレッジ ≥ 80%

**根拠**: 分岐カバレッジ80%は多くの業界標準（IEC 62304 Class B, MISRA等）で推奨される最低ライン。100%を目標にした場合のコスト効率が低下する領域（80-100%）は、リスクに応じて個別判断。

### コード重複率 ≤ 5%

**根拠**: Fowler (2018)「Refactoring」で示されるDRY原則。5%超過の重複は保守コストを著しく増加させる。SonarQube のデフォルト閾値 3% を参考に、許容範囲を5%に設定。

### 欠陥除去率（DRE） ≥ 95%

**根拠**: Capers Jones の業界調査データ。DRE 95%は高品質ソフトウェアの標準的な達成水準。85%未満は品質プロセスに重大な問題がある可能性を示唆。

---

## 曖昧語リスト（詳細版）

### 日本語

| カテゴリ | 曖昧語 | 推奨置換 |
|---------|--------|---------|
| 範囲の不明確 | 等、など、〜をはじめとする | 具体的に列挙する |
| 程度の不明確 | 適切に、十分な、高速な、大量の | 数値で定義する |
| 条件の不明確 | 必要に応じて、適宜、可能な限り | 条件を明示する |
| 頻度の不明確 | 通常は、基本的に、原則として | 例外条件を明記する |
| 近似値 | ほぼ、約、程度、前後 | 許容範囲を数値で定義する |
| 主体の不明確 | 〜される、〜が行われる（受動態） | 主語を明記する |

### 英語

| カテゴリ | 曖昧語 | 推奨置換 |
|---------|--------|---------|
| Scope | etc., and so on, such as | List exhaustively |
| Degree | appropriate, adequate, sufficient | Define numerically |
| Condition | as needed, if necessary, when possible | Specify conditions |
| Frequency | usually, normally, generally | State exceptions |
| Approximation | approximately, about, around | Define tolerance |
| Agency | it is done, shall be performed (passive) | Name the actor |

---

## メトリクス計測ツール推奨

| メトリクス | Python | JavaScript | Java | Go |
|----------|--------|-----------|------|-----|
| カバレッジ | coverage.py | istanbul/c8 | JaCoCo | go test -cover |
| 複雑度 | radon | escomplex | PMD | gocyclo |
| 重複率 | CPD（PMD） | jscpd | CPD（PMD） | dupl |
| 依存関係 | pydeps | madge | jdepend | go mod graph |
| 技術的負債 | SonarQube | SonarQube | SonarQube | SonarQube |
