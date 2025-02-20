import tkinter as tk
from tkinter import ttk
class PageSwitcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Page Switcher")
        self.geometry("400x300")

        # Create container frame
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store frames
        self.frames = {}

        # Create pages and store in frames dictionary
        for Page in (StartPage, PageOne, PageTwo):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")  # Show the first page initially

    def show_frame(self, page_name):
        """Bring the frame to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

# Define pages
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Start Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame("PageOne")).pack()
        tk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame("PageTwo")).pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        roomname = tk.Label(
            text=f"Un-Named Room",
            font=("Arial", 25)
        )
        output = tk.Text(
            self,
            bg="#EEEEEE"
            )
        roominfo = tk.Label(
            text=f"Connected to localhost on port 5000"
        )
        entry = tk.Text(
            self,
            bg="#EEEEEE",
            height=3
        )
        send = tk.Button(
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

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Page Two", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Start", command=lambda: controller.show_frame("StartPage")).pack()

if __name__ == "__main__":
    app = PageSwitcher()
    app.mainloop()
