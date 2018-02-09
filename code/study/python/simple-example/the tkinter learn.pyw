# tkinter
# 图形界面

from tkinter import *
import tkinter.messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameinput = Entry(self)
        self.nameinput.pack()
        self.alertbutton = Button(self,text = "hello",command = self.hello)
        self.alertbutton.pack()
    def hello(self):
        name = self.nameInput.get() or "world"
        tkinter.messagebox.showinfo("Message","hello,%s" %name)


root = Application()

root.mainloop()
