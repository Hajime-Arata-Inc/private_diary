# Web日記アプリ開発
## DjangoとPostgreSQLで開発したWebサイトで保存と投稿ができる日記アプリです
### 学習内容：Django・PostgreSQL・ターミナルの操作・Pytho3

## 機能一覧（実装済）

- ユーザー認証（ログイン／ログアウト）
  - Django標準の LoginView / LogoutView を拡張し、独自テンプレートに対応
  - ログアウト処理はセキュリティ対策として POST メソッドで実装
  - ログイン画面： `/login/`、ログアウト画面： `/logout/`（logged_out.html）

※詳細な経緯は [Issue #1](https://github.com/Hajime-Arata-Inc/private_diary/issues/1#issue-3160573850) を参照
