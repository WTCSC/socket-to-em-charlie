import tkinter as tk



# Main window
root = tk.Tk()
root.title("Main App")
root.geometry("400x300")

# Open Settings Button
open_button = tk.Button(root, text="Open Settings", command=open_settings)
open_button.pack(pady=20)

root.mainloop()
