# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- ゴール地点の追加：右下のマスにこうかとんの画像を描画した。
- ゴール判定の追加：こうかとんのマスまでいけたらゴールとし、移動できなくなるようにした。また、ゴール後にゴール地点のこうかとんが消えるようにした。
- 壁に移動しようとしたら?を浮かべているこうかとんの画像に変わるようにした。
- 移動したらその向きを向いているこうかとんが描画されるようにした。
- ゴール後に「ゴールしました」と出るようにした。
### ToDo（実装しようと思ったけど時間がなかった）
- ゴールしたときにshowinfoで知らせる
### メモ