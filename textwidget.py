import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.title("widget Example")
root.resizable(False, False)

text = tk.Text(root, height=8)
text.pack()
text.insert("1.0","Please enter a coment.. ")
text["state"]="normal"
scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
scroll.grid(row=0, column=1, sticky="ns ")
text["yscrollcommand"] = scroll.set
root.mainloop()