import tkinter as tk
import maze_maker as mm
import pygame
import queue
import copy
import time

def key_down(event):
    global key
    key = event.keysym
#C0A21071が実装
#キーを離しても押された状態を保つために、キーを話したときの関数を削除した
#def key_up(event):
 #   global key
  #  key = ""
  
def enemy_move():
    global ex,ey
    grid = copy.deepcopy(maze_lst)
    for vec in grid:
        for i in range(len(vec)):
            if vec[i]==1 or vec[i]==9:
                vec[i] = -7
            elif vec[i]==0:
                vec[i] = -9


def key_up(event):
    global key
    key = ""

#C0A21079が実装
def enemy_move():
    global ex,ey
    grid = copy.deepcopy(maze_lst)
    for vec in grid:
        for i in range(len(vec)):
            if vec[i]==1 or vec[i]==9:
                vec[i] = -7
            elif vec[i]==0:
                vec[i] = -9

    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]
    que = queue.Queue()
    que.put((mx,my))
    grid[mx][my]=0
    while not que.empty():
        tx,ty = que.get()
        for i in range(4):
            nx,ny = tx+XP[i], ty+YP[i]
            if grid[nx][ny]!=-9:
                continue
            grid[nx][ny] = grid[tx][ty] + 1
            if nx==ex and ny==ey:
                break
            que.put((nx,ny))
    for i in range(4):
        if grid[ex][ey]==grid[ex+XP[i]][ey+YP[i]]+1:
            ex,ey = ex+XP[i],ey+YP[i]
            break

def main_proc():
    global cx, cy, mx, my, ball

    if key == "Up":my -= 1 
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1   
    
    #迷路生成のリストを流用して玉の残数判定をする処理、以下89行目まで(C0A21007)
    #0が通路、1が壁、9は玉が消去済みの通路
    if(maze_lst[mx][my] == 0):#行先のマスが通路（まだ玉が消されていない）なら
        ball -= 1 #玉の残数変数を１減らす
        maze_lst[mx][my] = 9 #消去済みの通路として9を代入する

    #こうかとんが移動した先の玉を消す（実際には白い四角形を描画して隠している）
    canvas.create_rectangle(mx*40, my*40, mx*40+40, my*40+40, fill="white")

    cx, cy = mx*40+20, my*40+20 #移動後のこうかとんの座標

    canvas.coords("kokaton", cx, cy)

    canvas.lift("kokaton") #こうかとんを画面上で最も手前側に表示する

    enemy_move()
    
    cex, cey = ex*40+20, ey*40+20

    if mx==ex and my==ey:
        caralarm()
        return


    canvas.coords("enemy", cex, cey)

    if(ball == 0): #玉を全て回収した時にゲームクリアの処理を挟むと思うので、それ用の判定文です(C0A21007)
        pass

    root.after(100, main_proc)

def bgm():#BGMを付与(C0A21160が実装）
    pygame.mixer.init(frequency = 44100)  
    pygame.mixer.music.load("menuettm.mp3")    
    pygame.mixer.music.play(10) 

def caralarm():#死亡時音声(C0A21160が実装）
    pygame.mixer.init(frequency = 44100)  
    pygame.mixer.music.load("carstop.wav")    
    pygame.mixer.music.play(1) 

bgm()

def countdown(num): #カウントダウンする関数(C0A21047が実装）
    label['text'] = num #残り時間がlabelのtextになる
    if num > 0: #残り時間が0になるまで
        root.after(1000, countdown, num-1) #1秒ごとにcountdown関数を実行し、そのたびに時間を減らす

        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    #残り時間表示（C0A21047が実装）
    label = tk.Label(root,
                    fg="red",
                    font=("MSゴシック", "30", "normal")
                    )
    label.pack()

    countdown(200)
    
    canvas = tk.Canvas(root, width=1200, height=1000, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(30, 18)
    #print(maze_lst)


    ball = mm.show_maze(canvas, maze_lst) #迷路を描画するときに、設置された玉の数を取得
    print(ball)

    mx, my = 1, 16
    ex, ey = 1, 1
    cx, cy = mx*30+30, my*30+30
    tori = tk.PhotoImage(file="fig/1.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    teki = tk.PhotoImage(file="fig/4.png")
    canvas.create_image(cx, cy, image=teki, tag="enemy")
    key = ""
    root.bind("<KeyPress>", key_down)
    main_proc()
    root.mainloop()