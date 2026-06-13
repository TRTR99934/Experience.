import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")

# Create a Label widget with text
my_text = tk.Label(root, text="Hello, World!", font=("Arial", 16, "bold"))

# Place the text inside the window
my_text.pack()

root.mainloop()
