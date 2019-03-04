'''
Entry   单行文本输入
Text    多行文本输入          只支持少次几种图像格式(GIF,bmp)等,不支持 JPG\png,所以要插入这些图像需要用pil处理
都支持图像\富文本等格式

show输入时回显的字符
'''

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x500+30+30")

entryVar1 = tk.StringVar()
entryVar2 = tk.StringVar()


def callback():
    entryVar2.set(entryVar1.get())


entryVar1.trace("w", lambda a, b, c: callback())  # w当写入时调用callback

entry1 = tk.Entry(window, textvariable=entryVar1, show='*')
entry1.pack(pady=10)

entry2 = tk.Entry(window, textvariable=entryVar2)
entry2.pack(pady=10)


text = tk.Text(window)
text.pack(pady=10)

pic = Image.open('pic.png')
photo1 = ImageTk.PhotoImage(pic)

text.image_create(tk.END, image=photo1)
text.tag_configure('big', font=('Arial', 25, 'bold'))
text.insert(tk.END, "臭美", 'big')


ha = Image.open('ha.JPG')
photo2 = ImageTk.PhotoImage(ha)
text.image_create(tk.END, image=photo2)

window.mainloop()
