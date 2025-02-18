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

frame = tk.Frame(window)
frame.pack(expand=True)  # Centers the frame automatically

title = tk.Label(frame, text="Chat Room")
namelabel = tk.Label(frame, text="Enter Name")
nameentry = tk.Entry(frame, width= 20)
iplabel = tk.Label(frame, text="Enter IP")
ipentry = tk.Entry(frame, width = 16)
portlabel = tk.Label(frame, text="Port")
portentry = tk.Entry(frame, width = 6)
submit = tk.Button(
    frame, 
    text="Submit", 
    command=submit_name
    )
output = tk.Label(
    frame, 
    text="",
    foreground="red"
)

title.grid(row=0, column=0)
#namelabel.grid(row=1, column=0)
nameentry.grid(row=1, column=0)
#iplabel.grid(row=2, column=0)
ipentry.grid(row=2, column=0)
#portlabel.grid(row=3, column=0)
portentry.grid(row=2, column=1)
submit.grid(row=4, column=0)
output.grid(row=5, column=0)
window.mainloop()