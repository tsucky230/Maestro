> 📊 **このファイルの役割**: Mermaid記法を用いたUML図（ユースケース、シーケンス、クラス図など）の作成ルールと標準テンプレートを定義します。

# Mermaid UML図 規約

> このファイルは `AGENTS.md` Section 10 の内容を含みます。

---

## 10. Mermaid UML図 規約

### 設計・テスト工程で使用するUML図

各工程で **Mermaid記法** を使い、以下のUML図を作成すること:

| 工程 | 必須図 | 推奨図 |
|------|--------|--------|
| SWP.1 要求仕様 | ユースケース図 | — |
| SWP.2 方式設計 | コンポーネント図、シーケンス図 | 配置図 |
| SWP.3 詳細設計 | クラス図、状態遷移図 | アクティビティ図 |
| SWP.4 単体テスト | — | シーケンス図（モック連携） |
| SWP.5 結合テスト | シーケンス図 | — |

### Mermaid記法サンプル

#### ユースケース図（要求仕様）

```mermaid
graph LR
    User((ユーザー))
    Admin((管理者))
    
    User --> UC1[ログイン]
    User --> UC2[データ閲覧]
    User --> UC3[データ編集]
    Admin --> UC4[ユーザー管理]
    Admin --> UC1
    
    UC1 -.->|include| UC5[認証処理]
    UC3 -.->|extend| UC6[バリデーション]
```

#### シーケンス図（方式設計・結合テスト）

```mermaid
sequenceDiagram
    participant C as クライアント
    participant A as APIサーバー
    participant D as データベース
    
    C->>A: リクエスト送信
    A->>A: バリデーション
    A->>D: クエリ実行
    D-->>A: 結果返却
    A-->>C: レスポンス返却
```

#### クラス図（詳細設計）

```mermaid
classDiagram
    class BaseService {
        <<abstract>>
        #logger: Logger
        +execute()* Result
        #validate(input) bool
    }
    class UserService {
        -repository: UserRepository
        +execute() Result
        +findById(id) User
    }
    class UserRepository {
        <<interface>>
        +find(id) User
        +save(user) void
    }
    BaseService <|-- UserService
    UserService --> UserRepository
```

#### 状態遷移図（詳細設計）

```mermaid
stateDiagram-v2
    [*] --> 初期化
    初期化 --> アイドル: 初期化完了
    アイドル --> 処理中: リクエスト受信
    処理中 --> 完了: 処理成功
    処理中 --> エラー: 処理失敗
    完了 --> アイドル: 結果返却
    エラー --> アイドル: エラー処理完了
    エラー --> [*]: 致命的エラー
```
