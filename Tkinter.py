from tkinter import *
import pyttsx3



def voice():
    f=a.get()
    engine.say(f)
    engine.runAndWait()


top = Tk()

a = StringVar()

top.geometry("600x600")
label1= Label(top,text='Write the Word',fg='red',font=('Arial',20,'italic','bold')).place(x=200,y=200)
b = Button(top, text='Start', fg='black', bg='yellow', command=voice, font=('Bauhaus 93', 20, 'bold')).place(x=250,y=350)
text=Entry(top,textvariable=a).place(x=240,y=250)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
top.mainloop()
