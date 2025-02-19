import tkinter as tk

window = tk.Tk()
theme = "Pink"
fontsize = "Medium"

header = tk.Label(
    font=("Arial", 25),
    text="Settings"
)
genlabel = tk.Label(
    text="General",
    font=("Arial", 15),
    pady=10
)
servlabel = tk.Label(
    text="Server",
    font=("Arial", 15),
    pady=15
)
button_frame = tk.Frame(window)
themeselector = tk.Button(
    button_frame,
    text=theme,
    width=10
)
fontsize_button = tk.Button(
    button_frame,
    text=fontsize,
    width=10
)
buttonlabel = tk.Label(
    text="Themes"
)
cooldowntime = tk.Scale(
    from_=0,
    to=60,
    orient="horizontal",
    length=150
)
maxusers = tk.Scale(
    from_=2,
    to=10,
    orient="horizontal",
    length=150
)
maxlabel = tk.Label(
    text="Max Users"
)
cooldownlabel = tk.Label(
    text="Message Couldown (Seconds)"
)
header.pack()
genlabel.pack()
themeselector.pack(side="left", padx=5)  # Adds some spacing
fontsize_button.pack(side="left", padx=5)
button_frame.pack()
servlabel.pack()
cooldownlabel.pack()
cooldowntime.pack()
maxlabel.pack()
maxusers.pack()

window.mainloop()
