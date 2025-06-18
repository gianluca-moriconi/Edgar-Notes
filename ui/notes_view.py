import tkinter as tk

class NotesView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#404040")
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.label = tk.Label(self.frame, text="Appunti", font=("Arial", 16))
        self.label.grid(row=0, column=0, pady=10)

        self.text = tk.Text(self.frame)
        self.text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
