> 💻 **このファイルの役割**: プログラミング言語ごとのコーディング規約、TDDワークフロー、セキュリティ基準、テストダブル（モック/スタブ）の使用ルールを定義します。

# コーディング規約（TDD・品質・セキュリティ・テストダブル）

> このファイルは `AGENTS.md` Section 11, 12, 13, 14 の内容を含みます。

---

## 11. TDD（テスト駆動開発）ワークフロー

### 原則: Red → Green → Refactor

```
1. RED:    詳細設計書をインプットに、テストを先に書く（テストは失敗する）
2. GREEN:  テストを満たす最小限のコードを書く
3. REFACTOR: コード品質規約（Section 12）を満たすようリファクタリング
```

### 具体的な作業手順

#### Step 1: 詳細設計書からテスト仕様を作成

```
DET-001 の関数仕様 → UT-001 テストケースを作成
  - 正常系テスト
  - 異常系テスト（例外、バリデーションエラー）
  - 境界値テスト
```

#### Step 2: テストコードを先に実装（RED）

```python
# @trace UT-001
def test_create_user_with_valid_data():
    """正常系: 有効なデータでユーザーが作成されること"""
    service = UserService(mock_repository)
    result = service.create(name="テスト太郎", email="test@example.com")
    assert result.success is True
    assert result.user.name == "テスト太郎"
```

#### Step 3: テストを実行して失敗を確認（RED確認）

```bash
# テストが失敗することを確認
pytest tests/ -v  # すべて FAILED
```

#### Step 4: テストを通す最小限の実装（GREEN）

```python
# @trace DET-001, SRC-001
class UserService:
    """ユーザーサービス: ユーザーの作成・管理を行う"""
    def create(self, name: str, email: str) -> Result:
        # テストを通す最小限の実装
        ...
```

#### Step 5: テスト合格を確認

```bash
pytest tests/ -v  # すべて PASSED
```

#### Step 6: リファクタリング（REFACTOR）

- Section 12 のコード品質規約を適用
- テストが引き続きPASSすることを確認

---

## 12. コード品質規約

### 関数サイズ制限

| 項目 | 制限値 | 例外 |
|------|--------|------|
| 関数の行数 | **100行以内** | 変数の列挙（定数定義、enum等）は除外可 |
| サイクロマティック複雑度 (CC) | **50以内** | — |

### 制限超過時の対応

1. **意図を変えずに**関数を分割する
2. 分割した関数にも適切な名前とDocstringを付与する
3. トレーサビリティタグは分割先にも引き継ぐ
4. 分割後のテストが既存テストと同等のカバレッジを維持すること

### CC計測コマンド例

| 言語 | ツール | コマンド |
|------|--------|---------|
| Python | radon | `radon cc src/ -a -nc` |
| JavaScript/TypeScript | escomplex | `cr src/` |
| Java | PMD | `pmd check -d src/ -R category/java/design.xml` |
| C/C++ | lizard | `lizard src/` |
| Go | gocyclo | `gocyclo -over 50 .` |
| Rust | rust-code-analysis | `rust-code-analysis-cli -m -p src/` |

### Docstring規約

すべての関数・クラスに以下を含むDocstringを記述する（日本語で）:

```python
def calculate_price(base_price: int, tax_rate: float, discount: int = 0) -> int:
    """
    商品の税込価格を計算する。

    基本価格に税率を適用し、割引額を差し引いた最終価格を返す。
    価格は整数に切り上げる（消費者有利の端数処理）。

    @trace DET-003

    Args:
        base_price: 基本価格（税抜）。0以上の整数。
            制約: 0 <= base_price <= 999_999_999
        tax_rate: 税率。0.0〜1.0の範囲の浮動小数点数。
            制約: 0.0 <= tax_rate <= 1.0
            例: 消費税10% → 0.10
        discount: 割引額（税抜価格からの差引額）。デフォルト0。
            制約: 0 <= discount <= base_price

    Returns:
        税込最終価格（整数、切り上げ）。最小値は0。

    Raises:
        ValueError: base_priceが負の値の場合
        ValueError: tax_rateが0.0〜1.0の範囲外の場合
        ValueError: discountがbase_priceを超える場合
    """
```

---

## 13. セキュリティコーディング規約

### 言語別セキュリティ標準

対象プロジェクトの言語に応じて、以下のセキュリティコーディング標準を適用する:

| 言語 | 適用標準 | 要チェック観点 |
|------|---------|-------------|
| Python | [OWASP Python Security](https://owasp.org/www-project-python-security/) | インジェクション、デシリアライズ、パス操作 |
| JavaScript/TS | [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html) | XSS、プロトタイプ汚染、依存関係 |
| Java | [SEI CERT Oracle Coding Standard for Java](https://wiki.sei.cmu.edu/confluence/display/java) | 入力検証、例外処理、並行処理 |
| C/C++ | [SEI CERT C/C++ Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c) | バッファオーバーフロー、メモリ管理、整数オーバーフロー |
| Go | [OWASP Go Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Go_Security.html) | 入力検証、暗号化、エラー処理 |
| Rust | [Rust Secure Coding Guidelines](https://anssi-fr.github.io/rust-guide/) | unsafe使用制限、パニック回避 |

### 共通セキュリティルール（全言語）

1. **入力バリデーション**: すべての外部入力を信頼しない。型・範囲・長さ・形式を検証する
2. **出力エスケープ**: 出力先に応じたエスケープ（HTML、SQL、OS コマンド等）を行う
3. **認証・認可**: 最小権限の原則を適用する
4. **秘密情報**: ハードコードしない。環境変数またはシークレットマネージャーを使用する
5. **ログ**: 機密情報（パスワード、トークン、個人情報）をログに出力しない
6. **暗号化**: 非推奨アルゴリズム（MD5、SHA-1、DES等）を使用しない
7. **依存関係**: 既知の脆弱性を持つライブラリを使用しない（`agents/oss-and-compliance.md` 参照）

### セキュリティチェック自動化

```bash
# Python
bandit -r src/ -f json -o security-report.json
safety check --json --output security-report-deps.json

# JavaScript/TypeScript
npm audit --json > security-report.json

# Java
mvn dependency-check:check

# Go
govulncheck ./...
```

---

## 14. テストダブル規約（Mock / Stub / Driver）

### テストダブルの種類と使い分け

| 種類 | 目的 | 使用場面 |
|------|------|---------|
| **Mock** | 呼び出しの検証（期待する呼び出しがされたか） | 外部API呼び出し、メール送信等の副作用の検証 |
| **Stub** | 固定値の返却（テスト対象に必要な入力を提供） | DB問合せ結果の差し替え、設定値の固定化 |
| **Driver** | テスト対象を呼び出す側の代替 | 下位モジュール単体テスト時の上位呼出し模擬 |
| **Spy** | 実際の処理を実行しつつ呼び出しを記録 | ログ出力の検証、イベント発火の確認 |
| **Fake** | 簡易版の実装（インメモリDB等） | 統合テスト時のDB差し替え |

### テストダブル設計ルール

1. **Mock/Stubはインターフェースに対して作成する**（具象クラスに直接モックしない）
2. **テストダブルにもトレーサビリティタグを付与する**
3. **テストダブルの振る舞いをテスト仕様書に記載する**
4. **テストダブルが実際のインターフェース契約に準拠していることを確認する**

### テストダブル記述例（Python）

```python
# @trace UT-001 (Mock: UserRepository)
class MockUserRepository:
    """UserRepositoryのモック実装。テスト用に固定データを返す。"""
    
    def __init__(self):
        self.saved_users: list[User] = []
        self.find_called_count: int = 0
    
    def find(self, user_id: str) -> User | None:
        """Stub: 固定ユーザーを返す"""
        self.find_called_count += 1
        if user_id == "existing-id":
            return User(id="existing-id", name="テスト太郎")
        return None
    
    def save(self, user: User) -> None:
        """Mock: 保存呼出しを記録"""
        self.saved_users.append(user)
```

### テスト構成例

```
tests/
├── unit/                    # 単体テスト
│   ├── test_user_service.py
│   └── doubles/             # テストダブル
│       ├── mock_user_repository.py
│       └── stub_external_api.py
├── integration/             # 結合テスト
│   ├── test_user_flow.py
│   └── fakes/
│       └── fake_database.py
└── qualification/           # 適格性確認テスト
    └── test_requirements.py
```

---

## 29. 組み込みソフトウェア コーディング規約

> 組み込みプロジェクト（マイコン、RTOS使用等）に適用する追加規約。
> 詳細なチェックリストは `knowledge/embedded-constraints.md` を参照。

### 型安全性

| # | ルール | 検出方法 |
|---|--------|---------|
| 1 | 暗黙の型変換を禁止する（特に符号付き↔符号なし） | コンパイラ警告 `-Wconversion -Wsign-conversion` |
| 2 | 算術演算のオーバーフロー可能性を検査する | 静的解析（MISRA C Rule 10.x） |
| 3 | レジスタ幅を超える演算に対してキャスト明示 | コードレビュー |
| 4 | ポインタ演算は型サイズを明示する | MISRA C Rule 18.x |

### メモリ・リソースリーク防止

| # | ルール | 検出方法 |
|---|--------|---------|
| 1 | `malloc`/`free` の対応を静的解析で確認する | Cppcheck, Coverity |
| 2 | 例外パス・エラーリターンでのリソース解放漏れを検査する | コードレビュー + 静的解析 |
| 3 | セマフォ・ミューテックスの取得/解放の対称性を検査する | コードレビュー |
| 4 | 動的メモリ確保を禁止する場合、その方針を明記する | コーディングガイドライン |

### 低電力モード規約

コードレビュー時に以下を確認する（詳細は `knowledge/embedded-constraints.md` §8を参照）:

1. Sleep遷移前に不要なペリフェラルのクロック供給を停止しているか
2. 非接続GPIOがフローティング状態にならず、リーク電流を防止しているか
3. 復帰に必要な割込み/RTCが正しく有効化されているか
4. Sleep解除後にペリフェラルが正しく再初期化されているか

### 静的解析ツール推奨設定（C/C++）

```bash
# MISRA C:2012 準拠チェック
cppcheck --enable=all --std=c11 --suppress=missingInclude src/

# スタック使用量の静的見積もり
arm-none-eabi-gcc -fstack-usage -c src/*.c

# 型安全性チェック
gcc -Wall -Wextra -Wconversion -Wsign-conversion -Wcast-align src/*.c
```
