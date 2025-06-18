import tkinter as tk
import datetime

class CalendarView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#404040")
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.label = tk.Label(self.frame, text="Calendario", font=("Arial", 16))
        self.label.grid(row=0, column=0, pady=10)

        today = datetime.date.today()
        self.date_label = tk.Label(self.frame, text=f"Oggi: {today.strftime('%d/%m/%Y')}")
        self.date_label.grid(row=1, column=0, pady=10)
