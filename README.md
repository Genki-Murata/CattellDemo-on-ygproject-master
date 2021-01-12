# CattellDemo-on-ygproject-master

## 初回作業

#### ============================================================
#### コンソールで docker-compose
#### ============================================================

■ docker-compose.yml のあるフォルダに移動

cd [path]

■ docker-compose 実行

docker-compose up -d

※この時点でコンテナが作成され自動実行されるが、
　front（react）は node_modules がない為、エラーが出てコンテナが落ちる


以下、各コンテナで対応を行う


#### ============================================================
#### django マイグレーション
#### ============================================================

■web(django)コンテナでの作業の為、コンテナにアクセス

docker exec -it ygproject-master_web_1 bash

※ ygproject_web_1 はコンテナ名

■マイグレーション実行

python manage.py migrate

■ superuser の作成

python manage.py createsuperuser

■コンテナを抜ける

ctrl + D


#### ============================================================
#### テストユーザ作成（ブラウザ作業）
#### ============================================================

※管理者画面（127.0.0.1:8000/admin/）から、
Examineesテーブル、M_usersテーブルにテスト用ユーザを作成すること
