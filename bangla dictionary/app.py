from tkinter import *
import csv

top=Tk()
data=csv.reader(open("BengaliDictionary_93.csv","r",encoding="utf-8"))

def word():
    f=a.get()
    count=0
    cunt=0
    for row in data:
        if f==row[0]:
            m=row[1]    
            cunt=1
        elif f==row[1]:
            m=row[0]
            cunt=1    
        else:
            count=1
    if(cunt==1):
        t1.insert(END,m)
    else:
        t1.insert(END,"Not Found")

def exit():
    top.destroy()
    
def clear():
    t1.delete('1.0',END)

def clear2():
    text.delete(first=0,last=100)

def clear3():
    data.seek(0)


a=StringVar()
top.geometry("500x500")
bt1=Button(top,text="Search",fg='black',bg='grey',command=word,font=('arial',10,'bold'),pady=10).place(x=150,y=250)
bt2=Button(top,text="Exit",fg='black',bg='grey',command=exit,font=('arial',10,'bold'),pady=10).place(x=210,y=250)
bt3=Button(top,text='Clear',command=lambda:[clear(),clear2(),clear3],fg='black',bg='yellow',pady=10,font=('arial black',10,'bold')).place(x=200,y=150)

text=Entry(top,textvariable=a)
text.place(x=150,y=200)
t1=Text(top,height=2,width=20)
t1.place(x=140,y=280)

top.mainloop()
