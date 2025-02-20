import tkinter as tk
window = tk.Tk()
from tkinter import ttk

def openmain():
    messager = tk.Toplevel(window)  # Create a new window
    messager.title("Chat Room")

    roomname = tk.Label(
        messager,
        text=f"Un-Named Room",
        font=("Arial", 25)
    )
    output = tk.Text(
        messager,
        bg="#EEEEEE"
        )
    roominfo = tk.Label(
        messager,
        text=f"Connected to localhost on port 5000"
    )
    entry = tk.Text(
        messager,
        bg="#EEEEEE",
        height=3
    )
    send = tk.Button(
        messager,
        text=">",
        font=("Arial", 20),
        width=8,
        height=1
    )
    roomname.pack()
    roominfo.pack()
    output.pack(expand=True, fill="both", padx=20,pady=10)
    entry.pack(expand=True, fill="x", padx=20, pady=10, side="left")
    send.pack(side="left", padx=10)

opener = tk.Button(
    text="Open",
    command=openmain
)
opener.pack()
window.mainloop()