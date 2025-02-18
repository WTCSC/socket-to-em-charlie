import tkinter as tk

root = tk.Tk()

b1 = tk.Button(root, text='b1')
b2 = tk.Button(root, text='b2')
b1.grid(column=0, row=0)   # grid dynamically divides the space in a grid
b2.grid(column=1, row=0)   # and arranges widgets accordingly
root.mainloop()