import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.title("widget Example")
root.resizable(False, False)
check_button = ttk.Checkbutton(root, text="Click me")
check_button.pack()



root.mainloop()