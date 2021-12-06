from tkinter import *
from tkinter import messagebox

def info():
    messagebox.showinfo("Info","Nothing to show")



def new():
    window=Tk()
    window.geometry("400x400")
    bt1=Button(window,text="Show Info",command=info,fg='indigo',bg='yellow',font=("Times new roman",10,"italic")).place(x=150,y=100)
    window.mainloop()