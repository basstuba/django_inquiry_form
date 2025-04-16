# Django × docker × mysql の雛形

## 使用方法

1. 任意のディレクトリにクローン作成
2. コンテナ作成
    ```
    docker compose up -d --build
    ```
3. djangoコンテナに下記のコマンドで入る
    ```
    docker compose exec django bash
    ```
4. .env作成
    ```
    cp .env.example .env
    ```
5. シークレットキー作成
    ```
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```
6. 作成したシークレットキーを.envのSECRET_KEYの値にコピペ

## 各種コマンド

- アプリを追加
    ```
    python manage.py startapp アプリ名
    ```
- ディレクトリの移動
    ```
    mv 移動させたいディレクトリのパス 移動先のパス
    ```
- マイグレーション
    ```
    python manage.py migrate
    ```
> [!Note]
> **アプリの追加とマイグレーションはdjangoコンテナ内で実行**

## その他
- アプリの追加はsrc/appsにする
- アプリ追加後、settings.pyのINSTALLED_APPSに'apps.core',のように追記
