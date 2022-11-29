#moduleのインポート
import tkinter as tk
import tkinter.messagebox as tkm

#ボタンをクリックしたときの動作
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)
root = tk.Tk()
root.geometry("480x500")


entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=3)

#0~9までの数字を表示する
r = 1
c = 2
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    c -= 1
    if c == -1:
        r+=1
        c=2
    if num == 1:
        c = 1

#+と=を表示する
c = 4
r = 1
operators = ["C", "(", ")", "", "", "**2", "**3", "**", "+", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    r += 1

    #一番下まで記号が入ったら上まで戻り、1つ左に次の記号が入るようにする
    if r == 5:
        #一番下まで記号が入り、数字の真横の列だったら、上に戻らず、1つ左に次の記号が入るようにする
        if c < 4:
            #0の右側にきたら、0の左側に次の記号が入るようにする
            if c == 2:
                c = 0
                r = 4
                continue
            c -= 1
            r = 4
            continue
        r = 1
        c -= 1

root.mainloop()