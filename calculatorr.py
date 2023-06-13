from tkinter import*
root=Tk()
root.title('PYTHON')
root.geometry("200x250")
root.configure(bg="black")
root.iconbitmap("a.ico")
def clicked(num):
    first_num=t1.get()
    t1.delete(0,END)
    t1.insert(0,str(first_num)+str(num))
def add():
    first_number=t1.get()
    global first 
    first=first_number
    global math 
    math="add"
    t1.delete(0,END)
def sub():
    first_number=t1.get()
    global first 
    first=first_number
    global math 
    math="sub"
    t1.delete(0,END)
def mul():
    first_number=t1.get()
    global first 
    first=first_number
    global math 
    math="mul"
    t1.delete(0,END)
def div():
    first_number=t1.get()
    global first 
    first=first_number
    global math 
    math="div"
    t1.delete(0,END)   
def equal():
    second_num=t1.get()
    t1.delete(0,END)
    if math=="add":
        ans=(int(first)+int(second_num))
        t1.insert(0,str(ans))
    elif math=="sub":
        ans=(int(first)-int(second_num))
        t1.insert(0,str(ans))
    elif math=="mul":
        ans=(int(first)*int(second_num))
        t1.insert(0,str(ans))
    else:
        ans=(int(first)/int(second_num))
        t1.insert(0,str(ans))
def clear():
    t1.delete(0,END)
t1=Entry(width=31)
t1.place(x=5,y=50)
btn1=Button(text="7", height=1, width=4, command=lambda:clicked("7"))
btn2=Button(text="8",  height=1, width=4, command=lambda:clicked("8"))
btn3=Button(text="9",  height=1, width=4, command=lambda:clicked("9"))
btn4=Button(text="+",  height=1, width=4, command=add)
btn5=Button(text="4",  height=1, width=4, command=lambda:clicked("4"))
btn6=Button(text="5",  height=1, width=4, command=lambda:clicked("5"))
btn7=Button(text="6",  height=1, width=4, command=lambda:clicked("6"))
btn8=Button(text="-",  height=1, width=4, command=sub)
btn9=Button(text="1",  height=1, width=4, command=lambda:clicked("1"))
btn10=Button(text="2",  height=1, width=4, command=lambda:clicked("2"))
btn11=Button(text="3",  height=1, width=4, command=lambda:clicked("3"))
btn12=Button(text="x",  height=1, width=4, command=mul)
btn13=Button(text="/",  height=1, width=4, command=div)
btn14=Button(text="0",  height=1, width=4, command=lambda:clicked("0"))
btn15=Button(text="c",  height=1, width=4, command=clear)
btn16=Button(text="=",  height=1, width=4, command=equal)
btn1.place(x=10,y=80)
btn2.place(x=60,y=80)
btn3.place(x=110,y=80)
btn4.place(x=160,y=80)
btn5.place(x=10,y=120)
btn6.place(x=60,y=120)
btn7.place(x=110,y=120)
btn8.place(x=160,y=120)
btn9.place(x=10,y=160)
btn10.place(x=60,y=160)
btn11.place(x=110,y=160)
btn12.place(x=160,y=160)
btn13.place(x=10,y=200)
btn14.place(x=60,y=200)
btn15.place(x=110,y=200)
btn16.place(x=160,y=200)
root.mainloop()