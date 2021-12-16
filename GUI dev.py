import tkinter as TK
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

img = Image.open("pic.jpg")
test = ImageTk.PhotoImage(img)
label = Label(image=test)
label.image=test
label.pack(padx=100,pady=100)
root.mainloop()