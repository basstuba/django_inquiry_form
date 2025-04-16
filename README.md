# Django × docker × mysql の雛形

## 使用方法

1. 任意のディレクトリにクローン作成
    ```
    git clone git@github.com:basstuba/Django_sample.git
    ```
2. リポジトリ名変更
    ```
    mv Django_sample 新しいリポジトリ名
    ```
3. .env作成
    ```
    cp .env.example .env
    ```
4. コンテナ作成
    ```
    docker compose up -d --build
    ```
5. djangoコンテナに下記のコマンドで入る
    ```
    docker compose exec django bash
    ```
6. シークレットキー作成
    ```
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```
7. 作成したシークレットキーを.envのSECRET_KEYの値にコピペ

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
- アプリ追加後、アプリ/apps.pyのnameも'apps.core'のようにsettings.pyのINSTALLED_APPSと揃える
