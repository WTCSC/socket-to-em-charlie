import tkinter as tk
import socket
import threading
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def gui():
    global messageready
    global theme

    theme = 3
    messageready = True
    def open_settings():
        def change_theme():
            global theme
            if theme >5:
                theme +=1
            else:
                theme = 0

        settings_frame = tk.Frame(window, bg=primary, padx=10, pady=10, relief="raised", borderwidth=2)
        settings_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

        header = tk.Label(
            settings_frame,
            font=("Arial", 25),
            text="Settings",
            bg=primary,
            fg=accent2
            )
        genlabel = tk.Label(
            settings_frame,
            text="General",
            font=("Arial", 15),
            pady=10,
            bg=primary,
            fg=text
            )
        button_frame = tk.Frame(
            settings_frame, 
            bg=primary,
            )

        themeselector = tk.Button(
            button_frame, 
            text="Pink", 
            width=10, 
            command=change_theme,
            bg=accent2,
            fg=text2
            )
        fontsize_button = tk.Button(
            button_frame, 
            text="Medium", 
            width=10,
            bg=accent2,
            fg=text2
            )
        maxlabel = tk.Label(
            settings_frame, 
            text="Max Users", 
            bg=primary,
            fg=text
            )
        maxusers = tk.Scale(
            settings_frame, 
            from_=2, 
            to=10, 
            orient="horizontal", 
            length=150,
            bg=primary,
            fg=text2,
            highlightthickness=0,
            )
        cooldowntime = tk.Scale(
            settings_frame,
            from_=0, 
            to=60,
            orient="horizontal",
            length=150,
            bg=primary,
            fg=text2,
            highlightthickness=0
            )
        servlabel = tk.Label(
            settings_frame,
            text="Server",
            font=("Arial", 15),
            pady=15,
            bg=primary,
            fg=text
            )
        cooldownlabel = tk.Label(
            settings_frame,
            text="Message Cooldown (Seconds)",
            bg=primary,
            fg=text
            )
        close_button = tk.Button(
            settings_frame,
            text="Close",
            command=settings_frame.destroy,
            bg=accent2,
            fg=text2
            )
        

        header.pack()
        genlabel.pack()
        themeselector.pack(side="left", padx=5)
        fontsize_button.pack(side="left", padx=5)
        button_frame.pack()
        servlabel.pack()
        cooldownlabel.pack()
        cooldowntime.pack()
        maxlabel.pack()
        maxusers.pack()
        close_button.pack(pady=10)

        



        # Close Button

    def cooldown():
        time.sleep(cooldowntime.get())
    def submit():
        global ip
        global port
        if len(nameentry.get()) > 20:
            output.config(text="Name is too long")
        elif len(ipentry.get()) > 16:
            output.config(text="Invalid IP")
        else:
            ip = ipentry.get()
            port = portentry.get()
            client.connect((ip, int(port)))
            time.sleep(1)
    cooldown = threading.Thread(target=cooldown)
    def submitbuttonpressed():
        submit()
        time.sleep(1)
        openmain()



    def openmain():
        
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

        def sendmessage():
            name = nameentry.get()
            msg = messageentry.get("1.0", "end")
            outgoing = f"{name}: {msg}"
            client.send(outgoing.encode())
            messageentry.delete("1.0", "end")

        handler = threading.Thread(target=messagehandler)
        handler.start()

        messager = tk.Toplevel(window)  # Create a new window
        messager.title("Chat Room")
        handler = threading.Thread(target=messagehandler)
        handler.start
        roomname = tk.Label(
            messager,
            text=f"Un-Named Room",
            font=("Arial", 25)
        )
        chatoutput = tk.Text(
            messager,
            bg="#EEEEEE"
            )
        roominfo = tk.Label(
            messager,
            text=f"Connecting..."
        )
        messageentry = tk.Text(
            messager,
            bg="#EEEEEE",
            height=3
        )
        send = tk.Button(
            messager,
            text=">",
            font=("Arial", 20),
            width=8,
            height=1,
            command=sendmessage
        )
        roomname.pack()
        roominfo.pack()
        chatoutput.pack(expand=True, fill="both", padx=20,pady=10)
        messageentry.pack(expand=True, fill="x", padx=20, pady=10, side="left")
        send.pack(side="left", padx=10)
        # Post Connection stuff
        client.send(f"{nameentry.get()} has joined\n".encode())
        roominfo.config(text=f"Connected to {ip} on port {port}")



    global primary
    global accent
    global text
    global font
    global accent2
    global text2
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
    submitbutton = tk.Button( 
        text="Connect", 
        command=submitbuttonpressed,
        bg=accent2,
        fg=text2
        )
    output = tk.Label( 
        text="",
        bg=primary,
        foreground="red"
    )


    settings = tk.Button(
        text="Settings",
        command=open_settings,
        bg=accent2,
        fg=text2
    )

    title.pack()
    namelabel.pack()
    nameentry.pack()
    iplabel.pack()
    ipentry.pack()
    portlabel.pack()
    portentry.pack()
    submitbutton.pack()
    output.pack()
    settings.pack()
    window.mainloop()

    client.close()

t2 = threading.Thread(target=gui)

t2.start()
