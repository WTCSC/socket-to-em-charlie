
import tkinter as tk
import socket
import threading
import time
import psutil
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
theme = "Pink"

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x450")
        self.resizable(False, False)
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Connect, Host):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        def changetheme():
            themebutton.config(text="Theme: Pfdfd")
        tk.Frame.__init__(self, parent)
        title = tk.Label(
            self,
            font=("Arial", 25),
            text="Chat Room Maker",
            pady=20
        )
        connectbutton = tk.Button(
            self,
            text="Connect",
            height=5,
            width=35,
            command = lambda : controller.show_frame(Connect)
        )
        hostbutton = tk.Button(
            self,
            text="Host",
            height=5,
            width=35,
            command = lambda : controller.show_frame(Host)
        )
        themebutton = tk.Button(
            self,
            text=f"Theme: {theme}",
            command=changetheme,
            width=15
        )
        title.pack()
        connectbutton.pack(pady=40)
        hostbutton.pack()
        themebutton.pack(pady=10)# Theme button (Feature not complete)

     
# second window frame page1 
class Connect(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = tk.Label(
            self,
            font=("Arial", 25),
            text="Chat Room Maker",
            pady=20
        )
        returnbutton = tk.Button(
            self,
            text ="Return",
            command = lambda : controller.show_frame(StartPage)
        )
        namelabel = tk.Label(
            self,
            text="Name"
        )
        nameentry = tk.Entry(
            self,
            width=35
        )
        iplabel = tk.Label(
            self,
            text="IP Address"
        )
        ipentry = tk.Entry(
            self,
            width="35",
        )
        portlabel = tk.Label(
            self,
            text="Port",
        )
        portentry = tk.Entry(
            self,
            width=15
        )
        passwordlabel = tk.Label(
            self,
            text="Passwrod"
        )
        passwordentry = tk.Entry(
            self,
        )
        connectbutton = tk.Button(
            self,
            height=3,
            width=20,
            text="Connect",
            command=lambda: connect(ipentry.get(), portentry.get(), nameentry.get())
        )
        errorlabel = tk.Label(
            self,
            fg="Red",
            text=""
        )
        def connect(ip, port, name):
            def openmain():
                window = tk.Toplevel()  # creates a new window
                window.title("Chat Room")

                def messagehandler():
                    while True:
                        response = client.recv(1024).decode()
                        if not response:
                            break
                        if response[:8] == "ROOMNAME":
                            roomname.config(text=response[9:])
                        else:
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

                handler = threading.Thread(target=messagehandler, daemon=True)
                handler.start()
                password = passwordentry.get()
                roomname = tk.Label(
                    window,
                    text="Un-Named Room",
                    font=("Arial", 25)
                )
                chatoutput = tk.Text(
                    window,
                    bg="#EEEEEE"
                )
                roominfo = tk.Label(
                    window,
                    text="Connecting..."
                )
                messageentry = tk.Text(
                    window,
                    bg="#EEEEEE",
                    height=3
                )
                send = tk.Button(
                    window,
                    text=">",
                    font=("Arial", 20),
                    width=8,
                    height=1,
                    command=sendmessage
                )
                
                roomname.pack()
                roominfo.pack()
                chatoutput.pack(expand=True, fill="both", padx=20, pady=10)
                messageentry.pack(expand=True, fill="x", padx=20, pady=10, side="left")
                send.pack(side="left", padx=10)

                # Post Connection Updates
                client.send(f"&/{password}".encode())
                client.send(f"{nameentry.get()} has joined\n".encode())
                roominfo.config(text=f"Connected to {ip} on port {port}")

                def on_close():
                    try:
                        client.send("DISCONNECT".encode())  # Notify the server (optional)
                        client.close()  # Close the connection
                        print("Disconnected from server.")
                    except:
                        print("Error disconnecting.")
                    window.destroy()  # Close the chat window

                window.protocol("WM_DELETE_WINDOW", on_close)  # Bind the close event

            if 1024 <= int(port) <= 65535 and 7 <= len(ip) <= 15 and 3 <= len(name) <= 20 and name[:2] != "&/": # Checks if the port number is valid, IP is within the right length and makes sure the name is a reasonable length and doesnt start with &/
                            client.connect((ip, int(port)))
                            time.sleep(1)
                            openmain()
                            portentry.delete(0, 'end') # Clean out the entry boxes
                            ipentry.delete(0, 'end')
                            passwordentry.delete(0, 'end')
            else:
                errorlabel.config(text="ERROR: Invalid Input")
        title.pack()
        namelabel.pack(pady = 5)
        nameentry.pack(pady = 5)
        iplabel.pack(pady = 5)
        ipentry.pack(pady = 5)
        portlabel.pack(pady = 5)
        portentry.pack(pady = 5)
        passwordlabel.pack()
        passwordentry.pack()
        connectbutton.pack()
        errorlabel.pack()
        returnbutton.pack()

class Host(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Function to get available network adapters
        def get_ip_addresses():
            ip_addresses = {}
            for interface, addrs in psutil.net_if_addrs().items():
                for addr in addrs:
                    if addr.family == socket.AF_INET:  # IPv4 addresses only
                        ip_addresses[interface] = addr.address
            return ip_addresses

        ip_addresses = get_ip_addresses()
        iplist = ["Select Adapter"] + [f"{interface}: {ip}" for interface, ip in ip_addresses.items()]
        ipaddrlist = [ip for interface, ip in ip_addresses.items()]


        title = tk.Label(
            self,
            font=("Arial", 25),
            text="Chat Room Maker",
            pady=20
        )

        returnbutton = tk.Button(
            self,
            text="Return",
            command=lambda: controller.show_frame(StartPage)
        )

        namelabel = tk.Label(
            self,
            text="Room Name"
        )

        nameentry = tk.Entry(
            self,
            width=35
        )

        portlabel = tk.Label(
            self,
            text="Port",
        )

        portentry = tk.Entry(
            self,
            width=15
        )

        adapter_var = tk.StringVar(self)  # Create a variable for selection
        adapter_var.set("Select Adapter")  # Set default text

        ipselector = tk.OptionMenu(
            self, adapter_var, *iplist
        )
        ipselector.config(width=20)  # Adjust dropdown width
        passwordlabel = tk.Label(
            self,
            text="Password",
        )
        passwordentry = tk.Entry(
            self,
        )
        hostbutton = tk.Button(
            self,
            height=3,
            width=20,
            text="Host",
            command=lambda: hosting(nameentry.get(), portentry.get())
        )

        errorlabel = tk.Label(
            self,
            fg="Red",
            text=""
        )
        def hosting(roomname, port):
            server_thread = threading.Thread(target=startserver, args=(roomname, port), daemon=True)
            server_thread.start()  # Runs in a separate thread so UI doesn't freeze
            servinfo = tk.Toplevel() # Creatse a new window for the server info

            # GUI Widgets and setup
            servinfo.title("Server Info")
            servinfo.geometry("350x250")
            titlelabel = tk.Label(
                servinfo,
                text="Hosting Server...",
                font=("Arial", 15)
            )
            roomnametitle = tk.Label(
                servinfo,
                text=f"Room Name: {roomname}",
                font=("Arial", 12)
            )
            ipaddrlabel = tk.Label(
                servinfo,
                text=f"IP Address: {ipaddrlist[iplist.index(adapter_var.get())-1]}",
                font=("Arial", 12)
            )
            portlabel = tk.Label(
                servinfo,
                text=f"Port: {port}",
                font=("Arial", 12)
            )
            passwordlabel = tk.Label(
                servinfo,
                text=f"Password: {passwordentry.get()}",
                font=("Arial", 12)
            )
            titlelabel.pack(pady=5)
            roomnametitle.pack(pady=5)
            ipaddrlabel.pack(pady=5)
            portlabel.pack(pady=5)
            passwordlabel.pack(pady=5)

        def startserver(theroomname, port):
            clients = []  # List to store all connected clients
            # Function to handle each client connection
            def handle_client(client_socket, addr):
                print(f"New connection from {addr}")
                clients.append(client_socket)  # Add client to list
                while True:
                    try:
                        msg = client_socket.recv(1024).decode()
                        if not msg:
                            break  # Client disconnected
                        if msg[:2] == "&/":  # Checks if the message starts with these two characters to determine if its a configuration message
                            if msg[2:] == password:
                                client_socket.send(f"ROOMNAME:{theroomname}".encode())
                            else:
                                client_socket.close()
                        else:
                            print(f"Received from {addr}: {msg}")

                            # Send the received message to ALL connected clients (including the sender)
                            broadcast(msg)
                            print(clients)
                    except ConnectionResetError:
                        break  # Handle client disconnection

                print(f"Connection closed for {addr}")
                clients.remove(client_socket)  # Remove client from list when disconnected
                client_socket.close()

            # Function to broadcast message to all connected clients
            def broadcast(message):
                for client in clients:
                    try:
                        client.send(message.encode())
                    except:
                        clients.remove(client)  # Remove any dead connections

            hostname = socket.gethostname()
            host = ipaddrlist[iplist.index(adapter_var.get())-1]
            password = passwordentry.get()

            # Server setup
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = int(port)  # User inputs port number

            server.bind((host, port))
            server.listen(5)  # Allows up to 5 pending connections

            # Accept multiple clients
            while True:
                client, addr = server.accept()
                client_thread = threading.Thread(target=handle_client, args=(client, addr))
                client_thread.start()
                

        title.pack()
        namelabel.pack(pady = 5)
        nameentry.pack(pady = 5)
        portlabel.pack(pady = 5)
        portentry.pack(pady = 5)
        passwordlabel.pack()
        passwordentry.pack()
        ipselector.pack(pady=10)
        hostbutton.pack()
        errorlabel.pack()
        returnbutton.pack()
  
  
# Driver Code
app = tkinterApp()
app.mainloop()
