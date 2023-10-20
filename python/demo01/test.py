from tkinter import *
root = Tk()
root.geometry('750x400')
# button1=Button(text='测试测试测试',bg='blue',fg='yellow',bd=2,anchor=SW,activebackground='pink',activeforeground='white',height=2,width=8,underline=0,font=('华文行楷',20),padx=20,pady=30,state=ACTIVE,wraplength=120,justify=RIGHT,cursor='cross')
# button1.grid(row=4,column=7)

button2=Button(root,text='测试2',bg='purple',font=('华文行楷',20),fg='blue',width=8,height=5,anchor=E,padx=20)
button2.grid(row=4,column=1)

# picture=PhotoImage(file="E:\\1.gif")#必须是真正的gif图片！，单纯改变图片的格式改不了图片的本质，无法运行
# button3=Button(root,text='图片',image=picture,compound='left')
# button3.grid(row=2,column=5)

button4=Button(root,bitmap='question',bd=2)
button4.grid(row=1,column=5)

button5=Button(root,relief=SUNKEN,text='测试5')
button5.grid(row=1,column=4)

root.mainloop()