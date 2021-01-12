# CattellDemo-on-ygproject-master
<img width="600" alt="スクリーンショット" src="https://i.gyazo.com/cc0b2fb64ac045f0fccb65dd578d8776.png">

## 初回作業

#### ============================================================
#### コンソールで docker-compose
#### ============================================================

■ docker-compose.yml のあるフォルダに移動

cd [path]

■ docker-compose 実行

docker-compose up -d

以下、各コンテナで対応を行う


#### ============================================================
#### django マイグレーション
#### ============================================================

■web(django)コンテナでの作業の為、コンテナにアクセス

docker exec -it ygproject-master_web_1 bash

※ ygproject-master_web_1 はコンテナ名

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
M_usersテーブル、Examineesテーブルにテスト用ユーザを作成すること
