# 📓 Private Diary
- Djangoを学習しながら開発している「日記アプリ」です。ユーザー認証、投稿機能、データベース連携など、Webアプリ開発の基本要素を実践的に習得することを目的としています。
---
## 🚀 主な機能

- ユーザー認証（サインアップ / ログイン / ログアウト）
- 日記の投稿・編集・削除・一覧表示
- Django標準テンプレート + Bootstrap によるシンプルなUI
- PostgreSQL対応（開発ではSQLiteでも利用可能）
- Django管理画面でのデータ管理
---
## 🛠️ 技術スタック
- **バックエンド**: Django (Python 3.12)
- **データベース**: PostgreSQL（学習用途ではSQLiteも可）
- **フロントエンド**: HTML, CSS, Bootstrap
- **開発環境**: VS Code, GitHub, pip, venv

---

## 📂 ディレクトリ構成
```
private_diary/
├── config/ # プロジェクト設定
├── diary/ # アプリ本体（モデル・ビュー・テンプレートなど）
│ ├── templates/diary/
│ └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```
---

## ⚙️ セットアップ手順

### 1. リポジトリをクローン
```bash
git clone https://github.com/Hajime-Arata-Inc/private_diary.git
cd private_diary
```
### 2. 仮想環境を作成
`python -m venv venv`
`source venv/bin/activate`   # Mac / Linux
`venv\Scripts\activate`      # Windows
### 3. 必要パッケージをインストール
`pip install -r requirements.txt`
### 4. 環境変数を設定
- プロジェクトルートに `.env` ファイルを作成し、以下のように設定します：
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:password@localhost:5432/private_diary
```
### 5. マイグレーションを実行
`python manage.py migrate`
### 6. 開発サーバーを起動
`python manage.py runserver`
- ブラウザで http://127.0.0.1:8000/ にアクセスできます。
### 今後のロードマップ
- [x] 日記のCRUD機能
- [x] ユーザー認証
- [x] UI改善（Bootstrap適用）
- [ ] 分析機能（投稿件数や傾向の可視化）
- [ ] AWSやRenderを使ったデプロイ
### 📸 スクリーンショット
（今後、アプリ画面のスクリーンショットを追加予定）
### コントリビュート
- このプロジェクトは学習目的で作成しています。改善提案やアドバイスは Issue / Pull Request にて歓迎します。
### ライセンス
- 詳細は LICENSE をご確認ください。

- CodeQL gate test
