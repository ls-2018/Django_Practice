'''
单选按钮,只能有一个处于选中状态
'''

import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

var = tk.StringVar()
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()
var.set('A')


def printSelection():
    label.config(text='你已经选择了' + var.get())


printSelection()
r1 = tk.Radiobutton(window, text='选项A', variable=var, value='A', command=printSelection)
r1.pack()
r2 = tk.Radiobutton(window, text='选项B', fg='red', variable=var, value='B', command=printSelection)
r2.pack()
window.mainloop()
