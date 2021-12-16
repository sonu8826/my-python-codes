#import the required library
from tkinter import *

#Create an instance of window or frame
win= Tk()
win.geometry("700x400")

#Create two buttons
#Add padding in x and y axis

b1= Button(win, text= "Button1", font=('Poppins bold', 15))
b1.pack(padx=56, pady=45)

b2= Button(win, text= "Button2", font=('Poppins bold', 15))
b2.pack(pady=70)

b3= Button(win, text= "Button3", font= ('Poppins bold', 15))
b3.pack(padx=50, pady=80)

#Keep running the window
win.mainloop()