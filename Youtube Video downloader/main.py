from tkinter import *
from tkinter.filedialog import *
from pytube import YouTube



def dload():
    f=a.get()
    save_path = asksaveasfilename()
    YouTube(f).streams.filter(file_extension='mp4').first().download(save_path)
    label2= Label(top,text='Download Complete',bg='red',fg='white',font=('Arial',20,'italic','bold')).place(x=200,y=400)


top = Tk()

a = StringVar()

top.geometry("600x600")
top.title('YouTube Video Downloader')
label1= Label(top,text='Paste Link Below',bg='red',fg='black',font=('Bauhaus',30,'bold')).place(x=200,y=200)
b = Button(top, text='Download', fg='black', bg='yellow', command=dload, font=('Bauhaus 93', 20, 'bold')).place(x=200,y=300)
text=Entry(top,textvariable=a,width=50).place(x=200,y=250)
icon=PhotoImage(file='ytlogo.png')
top.iconphoto(True,icon)
top.config(background="red")

top.mainloop()
