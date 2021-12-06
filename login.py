from tkinter import *
from tkinter import messagebox
import mysql.connector
import window

top=Tk()

con=mysql.connector.connect(
host = "localhost",
user="sakib",
password="sakib123hasan",
database = "login"
)

def login():
    cursor = con.cursor()
    count=0
    u=a.get()
    p=b.get()
    query = cursor.execute("SELECT password FROM logintable WHERE username = '%s'" % u)
    results = cursor.fetchall()   
    if results:
        for result in results:
            if(p==result[0]):
                count=1
                messagebox.showinfo("User Login","Login Successfull!")
        
            else:
                messagebox.showinfo("User Login","Login Failed")
    if count==1:
        top.destroy()          
        window.new()

top.geometry("300x300")
top.title("User Login")
a=StringVar()
b=StringVar()


btn=Button(top,text="Login",command=login,bg="indigo",fg="black",font=("times new roman",12,"italic")).place(x=120,y=200)

lab1=Label(top,text="Username",fg="black",font=("times new roman",8,"bold"))
lab1.place(x=30,y=150)
lab2=Label(top,text="Password",fg="black",font=("times new roman",8,"bold"))
lab2.place(x=30,y=175)

en1=Entry(top,textvariable=a)
en1.place(x=90,y=150)
en2=Entry(top,textvariable=b,show="*")
en2.place(x=90,y=175)

top.mainloop()
