import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe") #window title
root.geometry("350x260")

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=0, column=1)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=0, column=2)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=0, column=3)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=1, column=1)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=1, column=2)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=1, column=3)

btn= tk.Button(root, text="", width= 15, height=5)
btn.grid(row=2, column=1)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=2, column=2)

btn= tk.Button(root, text="", width=15, height=5)
btn.grid(row=2, column=3)



root.mainloop()