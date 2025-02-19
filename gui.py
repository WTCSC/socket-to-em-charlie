import tkinter as tk
import socket
import threading
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def gui():
    theme = 3
    def open_settings():
        def change_theme():
            global theme
            if theme >5:
                theme +=1
            else:
                theme = 0
        # Create an overlay frame
        settings_frame = tk.Frame(window, bg="white", padx=10, pady=10, relief="raised", borderwidth=2)
        settings_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

        # Header
        header = tk.Label(settings_frame, font=("Arial", 25), text="Settings", bg="white")
        header.pack()

        # General Settings
        genlabel = tk.Label(settings_frame, text="General", font=("Arial", 15), pady=10, bg="white")
        genlabel.pack()

        button_frame = tk.Frame(settings_frame, bg="white")
        button_frame.pack()

        themeselector = tk.Button(button_frame, text="Pink", width=10, command=change_theme)
        fontsize_button = tk.Button(button_frame, text="Medium", width=10)
        
        themeselector.pack(side="left", padx=5)
        fontsize_button.pack(side="left", padx=5)

        # Server Settings
        servlabel = tk.Label(settings_frame, text="Server", font=("Arial", 15), pady=15, bg="white")
        servlabel.pack()

        cooldownlabel = tk.Label(settings_frame, text="Message Cooldown (Seconds)", bg="white")
        cooldownlabel.pack()
        
        cooldowntime = tk.Scale(settings_frame, from_=0, to=60, orient="horizontal", length=150)
        cooldowntime.pack()

        maxlabel = tk.Label(settings_frame, text="Max Users", bg="white")
        maxlabel.pack()

        maxusers = tk.Scale(settings_frame, from_=2, to=10, orient="horizontal", length=150)
        maxusers.pack()

        # Close Button
        close_button = tk.Button(settings_frame, text="Close", command=settings_frame.destroy)
        close_button.pack(pady=10)
    def messagehandler():
        print("Handler Online")
        while True:
            response = client.recv(1024).decode()
            if not response:
                break
            chatoutput.config(state="normal")
            chatoutput.insert("end", f"\n{response}")
            chatoutput.see("end")
            chatoutput.config(state="disabled")

    handler = threading.Thread(target=messagehandler)
    def submit():
        if len(nameentry.get()) > 20:
            output.config(text="Name is too long")
        elif len(ipentry.get()) > 16:
            output.config(text="Invalid IP")
        else:
            ip = ipentry.get()
            port = portentry.get()
            chatoutput.config(state="normal")
            chatoutput.insert("end", f"Connected to {ip} as {nameentry.get()}\n")
            chatoutput.config(state="disabled")

            client.connect((ip, int(port)))
            time.sleep(1)
            handler.start()
    def sendmessage():
        name = nameentry.get()
        msg = messageentery.get()
        outgoing = f"{name}: {msg}"
        client.send(outgoing.encode())
    


    # COLORS!!!
    if theme == 0:
        primary = '#212434'
        accent = '#3F446F'
        text = '#FCF483'
        font = 'Arial'
        accent2 = '#FCF483'
        text2 = '#000000'
    if theme == 1:
        primary = '#212434'
        accent = '#3F446F'
        text = '#FCF483'
        font = 'Arial'
        accent2 = '#FCF483'
        text2 = '#000000'
    if theme == 2:
        primary = '#212434'
        accent = '#3F446F'
        text = '#FCF483'
        font = 'Arial'
        accent2 = '#FCF483'
        text2 = '#000000'
    if theme == 3:
        primary = '#FFB5BB'
        accent = '#FEEEEC'
        text = '#FD7094'
        font = 'Arial'
        accent2 = '#FEEDF5'
        text2 = '#000000'
    if theme == 4:
        primary = '#000000'
        accent = '#000000'
        text = '#39FF14'
        font = 'Arial'
        accent2 = '#39FE14'
        text2 = '#000000'

    window = tk.Tk()
    window.resizable(False, False)
    window.title("Chat Room")
    window.geometry("450x400")
    window.configure(bg=primary)

    title = tk.Label(
        text="Chat Room",
        bg=primary,
        fg=accent2,
        font=(font, 25) 
        )
    namelabel = tk.Label(
        text="Enter Name",
        bg=primary,
        fg=text
        )
    nameentry = tk.Entry(
        width= 20,
        bg=accent,
        fg=text
        )
    iplabel = tk.Label(
        text="Enter IP",
        bg=primary,
        fg=text
        )
    ipentry = tk.Entry(
        width = 16,
        bg=accent,
        fg=text
        )
    portlabel = tk.Label(
        text="Port",
        bg=primary,
        fg=text,
        )
    portentry = tk.Entry(
        width = 6,
        bg=accent,
        fg=text
        )
    submit = tk.Button( 
        text="Connect", 
        command=submit,
        bg=accent2,
        fg=text2
        )
    output = tk.Label( 
        text="",
        bg=primary,
        foreground="red"
    )
    messageentery = tk.Entry(
        width= 30,
        bg=accent,
        fg=text,
    )
    sendbutton = tk.Button(
        text="Send",
        command=sendmessage,
        bg=accent2,
        fg=text2
    )
    chatoutput = tk.Text(
        state="disabled",
        height=10,
        bg=accent,
        fg=text,
        width=50
    )
    settings = tk.Button(
        text="Settings",
        command=open_settings
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
    messageentery.pack()
    sendbutton.pack()
    settings.pack()
    chatoutput.pack()
    window.mainloop()

    client.close()

t2 = threading.Thread(target=gui)

t2.start()
