# sudo apt search python3-tk
# windows默认有

import tkinter

window = tkinter.Tk()  # 显示的窗口
window['background'] = 'gray'
# 互殴屏幕的宽高
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

# 控件居中显示
w = 300
h = 300

x = ws / 2 - w / 2
y = hs / 2 - h / 2

window.title('第一个tkinter应用')

# 设置窗口的尺寸和位置
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# 创建Label对象,并将label放在窗口上,文本显示....
label = tkinter.Label(window, text='hello world!', bg='yellow', fg='red')
label.pack(fill=tkinter.X, padx=10, pady=10)

label = tkinter.Label(window, text='hello world2!', bg='yellow', fg='red')
label.place(x=100, y=100, width=200, height=200)

# pack 布局 pack(水平居中)
'''
    fill(水平填充;水平方向填充整个窗口,通过fill参数)
    padx(设置边距,)
    pady(垂直外边距)# 上下不重叠
    内边距 ipady,ipadx
    side 可以让多个控件按水平从左往右或从右往左排列(LEFT\RIGHT\TOP\BOTTOM)
    anchor   停靠位置,对应于东南西北以及四个角,  n,s,e,w,nw,sw,se,ne,center
    
'''

# place
'''
指定控件的位置
x           
y
width
height
'''

# grid
'''
row     当前行,从0开始
column  当前列,从0开始



from tkinter import *  
window = Tk() 
colours = ['red','green','orange','white','yellow','blue']

r = 0  

for c in colours:
    Label(window,text=c, relief=RIDGE,width=15).grid(row=r,column=2)
    r = r + 1
mainloop()

'''

tkinter.mainloop()
