import tkinter as tk
from ui.main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Edgar Notes - Gestore di Appunti")
    root.geometry("900x600")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = MainWindow(root)
    root.mainloop()
