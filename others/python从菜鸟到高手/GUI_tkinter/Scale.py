'''
滑块组件:支持水平\垂直
label='拖我',         标签文本,水平在上,垂直在右
from_=5,                最小值,也是起始值
length=200,              控件的长度
to=11,                  最大值,也是结束值
orient=tk.HORIZONTAL,   \VERTICAL
tickinterval=2,         刻度的步长
resolution=0.01,        能滑动的步长
command=printSelection1     回调函数    # 自动传当前的值
'''

import tkinter as tk

window = tk.Tk()
window.geometry('300x400')

label1 = tk.Label(window, bg='yellow', width=20)
label1.pack()


def printSelection1(v):
    label1.config(text='当前值：' + v)


scale1 = tk.Scale(window, label='拖我', from_=5, to=11, orient=tk.HORIZONTAL,
                  length=200, tickinterval=2, resolution=0.01, command=printSelection1)
scale1.pack(pady=10)

window.mainloop()
