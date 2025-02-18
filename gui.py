import tkinter as tk
name = ''
def submit_name():
    if len(nameentry.get()) > 20:
        output.config(text="Name is too long")
    else:
        name = nameentry.get()
        output.config(text="")




window = tk.Tk()
window.resizable(False, False)
window.title("Chat Room")
window.geometry("450x400")

title = tk.Label(text="Chat Room")
namelabel = tk.Label(text="Enter Name")
nameentry = tk.Entry(width= 20)
iplabel = tk.Label(text="Enter IP")
ipentry = tk.Entry(width = 16)
portlabel = tk.Label(text="Port")
portentry = tk.Entry(width = 6)
submit = tk.Button( 
    text="Submit", 
    command=submit_name
    )
output = tk.Label( 
    text="",
    foreground="red"
)

title.pack()
namelabel.pack()
nameentry.pack()
iplabel.pack()
ipentry.pack()
portlabel.pack()
portentry.pack()
submit.pack()
output.pack()
window.mainloop()