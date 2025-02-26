import tkinter as tk
import threading
import time
window = tk.Tk()
def gui():
    text = tk.Label(
        text="Connecting"
    )
    text.pack()
    window.mainloop()
    def animation():
        while True:
            time.sleep(0.5)
            text.config(text="Connecting.")
            time.sleep(0.5)
            text.config(text="Connecting..")
            time.sleep(0.5)
            text.config(text="Connecting...")
guithread = threading.Thread(target=gui)
                                 

