import tkinter as tk
from services.storage import load_notes, delete_note

class NotesListView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#e0e0e0", padx=10, pady=10)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.listbox = tk.Listbox(self.frame, font=("Courier New", 12))
        self.listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.listbox.bind("<Double-Button-1>", self.on_select)
        self.listbox.bind("<<ListboxSelect>>", self.on_highlight)
        self.frame.bind("<Configure>", self.adjust_font)

        self.delete_button = tk.Button(self.frame, text="Elimina Nota", command=self.delete_selected)
        self.delete_button.grid(row=1, column=0, pady=10)
        self.delete_button.grid_remove()

        self.notes = []
        self.load_callback = None
        self.base_font_size = 12

    def refresh(self):
        self.listbox.delete(0, tk.END)
        self.notes = load_notes()
        self.listbox.insert(tk.END, " ➕ Nuova Nota ")
        for note in sorted(self.notes, key=lambda x: x['timestamp'], reverse=True):
            
            #title = note['title'][:30].ljust(30)
            #timestamp = note['timestamp']
            #display = f" {title} {timestamp} "
            #self.listbox.insert(tk.END, display)

            title = note['title'][:40]
            timestamp = note['timestamp']

            # Calcola quanta larghezza rimane nella riga per il timestamp
            padding_total = 70  # cambia a piacere, dipende da font e larghezza finestra
            spaces = max(2, padding_total - len(title) - len(timestamp))
            display = f"{title}{' ' * spaces}{timestamp}"

            self.listbox.insert(tk.END, f"  {display}  ")


        
        self.delete_button.grid_remove()

    def on_select(self, event):
        if self.load_callback:
            index = self.listbox.curselection()
            if index:
                if index[0] == 0:
                    self.load_callback(None)
                else:
                    note_data = sorted(self.notes, key=lambda x: x['timestamp'], reverse=True)[index[0] - 1]
                    self.load_callback(note_data)

    def on_highlight(self, event):
        index = self.listbox.curselection()
        if index and index[0] > 0:
            self.delete_button.grid()
        else:
            self.delete_button.grid_remove()

    def delete_selected(self):
        index = self.listbox.curselection()
        if index and index[0] > 0:
            note_data = sorted(self.notes, key=lambda x: x['timestamp'], reverse=True)[index[0] - 1]
            delete_note(note_data["id"])
            self.refresh()

    def set_note_loader(self, callback):
        self.load_callback = callback

    def adjust_font(self, event):
        width = max(event.width, 300)
        new_size = max(8, int(width / 60))
        self.listbox.config(font=("Courier New", new_size))
