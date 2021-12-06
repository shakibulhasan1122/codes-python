from tkinter import *
from PIL import ImageTk,Image

top=Tk()

top.geometry("900x700")
canv=Canvas(top,height=800,width=650)
canv.pack()
m=input("Enter File path")
myImg=ImageTk.PhotoImage(Image.open(m)) 
canv.create_image(20,20, anchor=NW, image=myImg)      
top.mainloop()