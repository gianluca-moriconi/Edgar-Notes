import tkinter as tk                            # importa la libreria tkinter
from ui.main_window import MainWindow           # importa la classe MainWindow

if __name__ == "__main__":
    root = tk.Tk()                              # Crea la finestra principale

    # Dimensioni dello schermo: 60% 
    screen_width = root.winfo_screenwidth()     # Ottiene la larghezza dello schermo
    screen_height = root.winfo_screenheight()   # Ottiene l'altezza dello schermo
    width = int(screen_width * 0.6)             # Calcola la larghezza della finestra
    height = int(screen_height * 0.6)           # Calcola l'altezza della finestra
    x = int((screen_width - width) / 2)         # Calcola la posizione x dove posizionare la finestra
    y = int((screen_height - height) / 2)       # Calcola la posizione y dove posizionare la finestra
    root.geometry(f"{width}x{height}+{x}+{y}")  # Crea una finestra con le dimensioni e la posizione specificate

    root.minsize(600, 400)                      # Imposta la dimensione minima della finestra

    app = MainWindow(root)                      # Crea una istanza della classe MainWindow
    root.mainloop()                             # Avvia l'applicazione