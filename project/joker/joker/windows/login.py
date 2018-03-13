# this is login windows

import tkinter as tk
from tkinter import *

def reg():
    s1 = e1.get()
    s2 = e2.get()
    t1 = len(s1)
    t2 = len(s2)

    if s1 == "zzp" and s2 == "joker":
        c["text"] = "登陆成功！"
    else:
        c["text"] = "用户名或密码错误!"
        e1.delete(0,t1)
        e2.delete(0,t2)
    return

#获取屏幕的宽和高
def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()
    return window.winfo_screenwidth(),window.winfo_screenheight()

# 获取窗口的宽和高
def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()
    return window.winfo_reqwidth(),window.winfo_reqheight()

def center_window(root,width,height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)
    return

root = tk.Tk()
root.title("Login")
root.resizable(0,0)
center_window(root,400,200)
#root.geometry('400x200+500+100')
root.iconbitmap('D:\\zzp\\code\\python\\icons\\joker.ico')

l = Label(root,text ="用户名：")
l.grid(row = 0,column = 0,sticky = W)

e1 = Entry(root)
e1.grid(row = 0,column = 1,sticky = E)

l2 = Label(root,text = "密码：")
l2.grid(row = 1,column = 0,sticky = W)

e2 = Entry(root)
e2['show'] = "*"
e2.grid(row = 1,column = 1,sticky = E)

b = Button(root,text = "登录",command = reg)
b.grid(row = 2,column = 1,sticky = E)

c = Label(root,text = "")
c.grid(row = 3,column = 1,sticky = E)

root.mainloop()
