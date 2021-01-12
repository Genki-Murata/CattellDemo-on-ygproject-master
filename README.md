# CattellDemo-on-ygproject-master
<img width="400" alt="スクリーンショット" src="https://i.gyazo.com/cc0b2fb64ac045f0fccb65dd578d8776.png">

# 初回作業

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
#### SQL追加対応
#### ============================================================

■コンソールからdockerコンテナに接続

docker exec -it ygproject-master_db_1 bash

※ ygproject-master_db_1 はコンテナ名

■psqlログイン

psql -U postgres

■テスト集計用データ登録

INSERT
  INTO
    ygtestapp_m_result (
      criteria
      ,item_no
      ,feature_group_id
      ,feature_group_top
      ,feature_group_bottom
      ,feature_detail_id
      ,feature_detail_top
      ,feature_detail_bottom
      ,delete_flag
      ,create_date
      ,update_date
    )
  VALUES
    ('A','2','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('AG','6','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('C','11','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('Co','7','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('D','12','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('G','1','5','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('I','10','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('N','9','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('O','8','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('R','1','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('S','1','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now()),
    ('T','3','1','特徴グループ 表','特徴グループ 裏','1','性格特徴 表','性格特徴 裏',false,now(),now());

※ INSERT 0 12 の表示でOK

■テスト集計用データ登録

INSERT
  INTO
    ygtestapp_m_question (
      question_id
      ,question
      ,delete_flag
      ,create_date
      ,update_date
      ,criteria_id
    )
  VALUES
    ('1','色々な人と知り合いになるのが楽しみである',false,now(),now(),'S'),
    ('2','人中ではいつも後の方に引込んでいる',false,now(),now(),'A'),
    ('3','むずかしい問題を考えるのが好きである',false,now(),now(),'T'),
    ('4','色々違う仕事がしてみたい',false,now(),now(),'R'),
    ('5','周囲の人とうまく調子をあわせていく',false,now(),now(),'G'),
    ('6','いつも何かしていないと気がすまない',false,now(),now(),'AG'),
    ('7','世の中の人は人のことなどかまわないと思う',false,now(),now(),'Co'),
    ('8','わけもなく喜んだり悲しんだりする',false,now(),now(),'O'),
    ('9','人が見ていると仕事ができない',false,now(),now(),'N'),
    ('10','失敗しやしないかといつも心配である',false,now(),now(),'I'),
    ('11','気持を顔にあらわしやすい',false,now(),now(),'C'),
    ('12','時々何に対しても興味がなくなる',false,now(),now(),'D');

※ INSERT 0 12 の表示でOK


#### ============================================================
#### テストユーザ作成（ブラウザ作業）
#### ============================================================

※管理者画面（127.0.0.1:8000/admin/）から、
M_usersテーブル、Examineesテーブルにテスト用ユーザを作成すること
