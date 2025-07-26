# クライアント用管理画面付お問い合わせフォーム

## アプリケーション概要

Laravelを学習した際に作成した課題を学習のアウトプットのためにDjangoで作成した

## アプリケーションURL

ユーザー用トップページ
```
http://localhost:8000/core/
```
クライアント用ログイン画面
```
http://localhost:8000/accounts/login/
```
管理者用ログイン画面
```
http://localhost:8000/admin/
```

## 機能一覧

### クライアントが利用可能な機能

- ログイン及びログアウト機能

- 管理者アカウント作成機能

- お問い合わせ一覧表示機能

- お問い合わせ検索機能

- お問い合わせ削除機能

- エクスポート機能

- ページネーション機能

### ユーザーが利用可能な機能

- お問い合わせ送信機能

- お問い合わせ内容確認画面表示機能

- サンクスページ表示機能

## 使用方法

1. 任意のディレクトリにクローン作成
    ```
    git clone git@github.com:basstuba/django_inquiry_form.git
    ```
2. リポジトリ名変更
    ```
    mv django_inquiry_form 新しいリポジトリ名
    ```
3. .env作成
    ```
    cp .env.example .env
    ```
4. コンテナ作成
    ```
    make up
    ```
5. シークレットキー作成
    ```
    make secretkey
    ```
6. 作成したシークレットキーを.envのSECRET_KEYの値にコピペ

7. マイグレーションファイル作成
    ```
    make makemigrations
    ```

8. マイグレーション
    ```
    make migrate
    ```

9. ダミーデータ作成（任意）
    ```
    make factory
    ```

10. 管理者用アカウント作成（任意）
    ```
    make createsuperuser
    ```

## ローカル環境に仮想環境を作成（VS Code の補完・警告解消用のため任意）

1. 下記のコマンドで作成
    ```
    make venv
    ```
2. VS Codeを再起動して、VS Code下部のPythonバージョンを **.venv** のものに設定

## 各種コマンド

- Makefile参照

## その他
- ダミーデータは50件作成することができます
