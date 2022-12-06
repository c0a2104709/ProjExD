import tkinter as tk
import maze_maker
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, kokaton, goal
    goal = tk.PhotoImage(file="fig/9.png") #右下のマスにゴール地点としてこうかとんの画像を描画
    canvas.create_image(13*100+50, 7*100+50,
                        image=goal,
                        tag="goal")
    if key ==  "Up":
        kokaton = tk.PhotoImage(file="fig/6.png")#上を向いているこうかとんの画像を描画
        my -= 1
    if key == "Down":
        kokaton = tk.PhotoImage(file="fig/4.png")#下を向いているこうかとんの画像を描画
        my += 1
    if key == "Left":
        kokaton = tk.PhotoImage(file="fig/5.png")#左を向いているこうかとんの画像を描画
        mx -= 1
    if key == "Right":
        kokaton = tk.PhotoImage(file="fig/2.png")#右を向いているこうかとんの画像を描画
        mx += 1
    if maze_lst[mx][my] == 1: #移動先が壁だったら
        kokaton = tk.PhotoImage(file="fig/0.png") #?を浮かべているこうかとんの画像を描画
        if key ==  "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, 
                        image=kokaton, 
                        tag="kokaton")
    canvas.coords("kokaton", cx, cy)
    if cx == 13*100+50 and cy == 7*100+50: #右下のマスについたら終了させる
        goal = None
        tkm.showinfo("ゴール", "ゴールしました")
        return
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width= 1500, height=900, bg="black")
    canvas.pack()
    maze_lst = maze_maker.make_maze(15, 9)
    #print(maze_lst)
    maze_maker.show_maze(canvas, maze_lst)
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    kokaton = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, 
                        image=kokaton, 
                        tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()