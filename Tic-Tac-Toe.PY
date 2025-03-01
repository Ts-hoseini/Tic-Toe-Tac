import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe") #window title
root.geometry("300x300")

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=0, column=1)

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=0, column=2)

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=0, column=3)

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=1, column=1)

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=1, column=2)

btn= tk.Button(root, text="", width=10, height=2)
btn.grid(row=1, column=3)

btn= tk.Button(root, text="", width= 10eight=2)
btn.grid(row=2, column=1)

btn= tk.Button(root, text="", width=7, height=2)
btn.grid(row=2, column=2)

btn= tk.Button(root, text="", width=7, height=2)
btn.grid(row=2, column=3)



root.mainloop()