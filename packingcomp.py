import tkinter as tk

# -- Aligning with `side` ---

root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="y", expand=True)
tk.Label(root, text="Label 2", bg="red").pack(side="left")

root.mainloop()

# -- Filling in one direction --

root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="y")
tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="x")

root.mainloop()

# -- Filling in both directions --

root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="both")
tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="both")

root.mainloop()


# -- Even if either label doesn't fill --

root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left")
tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="both")

root.mainloop()


root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="both")
tk.Label(root, text="Label 2", bg="red").pack(side="top")

root.mainloop()

# -- expand can make it grow as much as possible. It won't hide other widgets, but other widgets will be compressed --

root = tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", expand=True, fill="both")
tk.Label(root, text="Label 2", bg="red").pack(side="top")

root.mainloop()


# -- expanding two widgets means they share the available space evenly --

root = tk.Tk()

tk.Label(root, text="Label 2", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label 2", bg="red").pack(side="top", expand=True, fill="both")

root.mainloop()


# -- whichever side comes first gets expansion priority --

root = tk.Tk()

tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")

root.mainloop()

root = tk.Tk()

tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)

root.mainloop()
