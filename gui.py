import tkinter as tk
import socket
import threading
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def gui():

    def messagehandler():
        print("Handler Online")
        while True:
            response = client.recv(1024).decode()
            if not response:
                break
            chatoutput.config(state="normal")
            chatoutput.insert("end", f"{response}\n")
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
    primary = '#212434'
    accent = '#3F446F'
    text = '#BBBBBB'
    font = 'Arial'

    window = tk.Tk()
    window.resizable(False, False)
    window.title("Chat Room")
    window.geometry("450x400")
    window.configure(bg=primary)

    title = tk.Label(
        text="Chat Room",
        bg=primary,
        fg=text,
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
        command=submit
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
        command=sendmessage
    )
    chatoutput = tk.Text(
        state="disabled",
        height=10,
        bg=accent,
        fg=text,
        width=50
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
    chatoutput.pack()
    window.mainloop()

    client.close()

t2 = threading.Thread(target=gui)

t2.start()
