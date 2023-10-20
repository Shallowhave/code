import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class application(Frame):
    def __init__(self, master=None) :
        super().__init__(master)
        self.master=master
        self.pack(anchor=NW)
        self.createWidget()
    def createWidget(self):
        file_btn=Button(self,text='文件(F)',command=self.open_file_dialog)
        file_btn.pack(side='left')

        edit_btn=Button(self,text='编辑(E)',command=self.songhua,justify='left')
        edit_btn.pack(side='left')

        format_btn=Button(self,text='格式(O)',command=self.songhua,justify='left')
        format_btn.pack(side='left')

        view_btn=Button(self,text='查看(V)',command=self.songhua,justify='left')
        view_btn.pack(side='left')

        help_btn=Button(self,text='帮助(H)',command=self.songhua,justify='left')
        help_btn.pack(side='left')
        # str = StringVar()
        # self.str = Entry(self,textvariable=str)
        self.text = Text(height=300,width=1000)
        self.text.pack(anchor=NW,pady=1)

    def songhua(self):
        messagebox.showinfo("测试","功能完善中...")
    def open_file_dialog(self):
        filename = filedialog.askopenfilename()
        if self.is_file_open(filename=filename):
            messagebox.showinfo(filename)
    def is_file_open(self,filename):
        try:
        # 使用 os.access() 函数检查文件是否可访问
            os.access(filename, os.W_OK)
            return False
        except PermissionError:
            return True
        
        
        



# if __name__ == '__mian__':
root = Tk()
root.title("记事本")
root.iconbitmap("D:\\code\\python\\demo01\icon\\nodepad.ico")

root.geometry("1100x700+370+200")
app = application(root)
root.mainloop()