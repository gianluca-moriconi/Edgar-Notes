import tkinter as tk
from tkinter import PhotoImage  
import datetime

class WelcomeView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#404040")
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)


        today = datetime.date.today()
        self.date_label = tk.Label(self.frame, text=f"Oggi: {today.strftime('%d/%m/%Y')}")
        self.date_label.grid(row=0, column=0, pady=10)


        self.logo_img = PhotoImage(file="assets/icons/logo_edgar.png")
        self.logo_label = tk.Label(self.frame, image=self.logo_img, bg="#404040")
        self.logo_label.grid(row=1, column=0, pady=10)


        #self.label = tk.Label(self.frame, text="Edgar Notes", font=("Arial", 26))
        #self.label.grid(row=1, column=0, pady=10)

        