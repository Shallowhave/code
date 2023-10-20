import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from flask import Flask

class application(Frame):
    def __init__(self, master=None) :
        super().__init__(master)
        self.master=master
        self.pack(anchor=NW)
        self.createWidget()
    def createWidget(self):
        But_text=(("MC","MR","M+","M-"),
                  ("%","CE","C","×"),
                  ("7","8","9","×"),
                  ("4","5","6","-"),
                  ("1","2","3","+"),
                  ("±","0",".","="))
        self.entry = Entry(self)
        self.entry.grid(row=0,column=0,columnspan=4,pady=5)
        for i,v in enumerate(But_text):
            for i2,v2 in enumerate(v):
                Button(self,text=v2,width=10,height=3).grid(row=i+1,column=i2,sticky=NSEW)

        
        
        



# if __name__ == '__mian__':
root = Tk()
root.title("计算器")
root.iconbitmap("D:\\code\\python\\demo01\icon\\nodepad.ico")

root.geometry("320x500+370+200")
app = application(root)
root.mainloop()