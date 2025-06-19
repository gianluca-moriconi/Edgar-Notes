import tkinter as tk
from services.storage import save_note, update_note

class NotesView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)

        self.current_note_id = None
        self.base_font_size = 12

        #self.title_label = tk.Label(self.frame, text="Titolo:", font=("Arial", self.base_font_size))
        #self.title_label.grid(row=0, column=0, sticky="w", padx=(10, 5), pady=(10, 0))

        self.title_entry = tk.Entry(self.frame, font=("Arial", self.base_font_size), fg="gray")
        self.title_entry.insert(0, "Titolo")
        self.title_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")
        self.title_entry.bind("<FocusIn>", self.clear_placeholder)
        self.title_entry.bind("<FocusOut>", self.add_placeholder)

        self.text = tk.Text(self.frame, font=("Arial", self.base_font_size), padx=10, pady=10)
        self.text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.save_button = tk.Button(self.frame, text="Salva", command=self.save_note, font=("Arial", self.base_font_size))
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.frame.bind("<Configure>", self.adjust_fonts)

    def save_note(self):
        title = self.title_entry.get().strip()
        if title == "Titolo":
            title = ""
        title = title or "Senza titolo"
        content = self.text.get("1.0", "end-1c").strip()
        if content:
            if self.current_note_id:
                update_note(self.current_note_id, title, content)
            else:
                save_note(title, content)
            self.clear_editor()

    def load_note(self, note_data):
        self.clear_editor()
        self.current_note_id = note_data["id"]
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, note_data["title"])
        self.title_entry.config(fg="black")
        self.text.insert("1.0", note_data["content"])

    def clear_editor(self):
        self.current_note_id = None
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "Titolo")
        self.title_entry.config(fg="gray")
        self.text.delete("1.0", tk.END)

    def clear_placeholder(self, event):
        if self.title_entry.get() == "Titolo" and self.title_entry.cget("fg") == "gray":
            self.title_entry.delete(0, tk.END)
            self.title_entry.config(fg="black")

    def add_placeholder(self, event):
        if not self.title_entry.get():
            self.title_entry.insert(0, "Titolo")
            self.title_entry.config(fg="gray")

    def adjust_fonts(self, event):
        width = max(event.width, 400)
        new_size = max(9, int(width / 60))
        #self.title_label.config(font=("Arial", new_size))
        self.title_entry.config(font=("Arial", new_size))
        self.text.config(font=("Arial", new_size))
        self.save_button.config(font=("Arial", new_size))
