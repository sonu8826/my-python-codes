import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

except:
    pass

def entry():

    print(f"Hello, {user_name.get()}")
    print(f"Timing:{user_timing.get()}")
    print(f"Roll.no:{user_roll.get()}")
    print(f"Register successfully")

root = tk.Tk()
root.title("Entry")
root.geometry("600x90")
root.resizable(False, False)


user_name = tk.StringVar()
user_timing = tk.StringVar()
user_roll = tk.StringVar()


input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")
name_label = ttk.Label(input_frame, text="Name:")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

timing_label = ttk.Label(input_frame, text="Timing:")
timing_label.pack(side="left", padx=(0, 10))
timing_entry = ttk.Entry(input_frame, width=15, textvariable=user_timing)
timing_entry.pack(side="left")
timing_entry.focus()

roll_label = ttk.Label(input_frame, text="Roll.no:")
roll_label.pack(side="left", padx=(0, 10))
roll_entry = ttk.Entry(input_frame, width=15, textvariable=user_roll)
roll_entry.pack(side="left")
roll_entry.focus()

buttons = ttk.Frame(input_frame, padding=(20, 10))
buttons.pack(fill="both")

entry_button = ttk.Button(root, text="Enter", command=entry)
entry_button.pack(side="left", fill="x", expand="true")
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand="true")

root.mainloop()