# 动态获取和设置Label的内容

import tkinter as tk

window = tk.Tk()
window.geometry("300x200+30+30")


var = tk.StringVar()    # 动态
var.set('Hello World')
label2 = tk.Label(window, textvariable=var, fg='blue', bg='yellow', font=('Arial', 12), width=15, height=2)
label2.pack(pady=20)


onHit = False

def hitMe():
    global onHit
    if onHit == False:
        onHit = True
        var.set('世界你好')
    else:
        onHit = False
        var.set('Hello World')


button1 = tk.Button(window, text='点击我', command=hitMe)
button1.pack()


def getLabelText():
    print(var.get())


button2 = tk.Button(window, text='获取Label控件的文本', command=getLabelText)
button2.pack(pady=20)

window.mainloop()
