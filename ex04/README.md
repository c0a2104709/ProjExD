# 第4回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- 5秒後に2倍の速さで動く青い爆弾が追加される
- 10秒後に3倍の大きさの緑の爆弾が追加される
- 60秒タイマーを表示
- 60秒爆弾に当たらなかったら、CLEARと表示
### ToDo（実装しようと思ったけど時間がなかった）
- 爆弾に当たったときにgameoverなどの文字を表示する
- if文をまとめる