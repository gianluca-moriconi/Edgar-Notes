import tkinter as tk
from tkinter import PhotoImage
from ui.welcome_view import WelcomeView
from ui.notes_view import NotesView
from ui.notes_list_view import NotesListView

class MainWindow:
    def __init__(self, root):
        self.root = root

        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=0)  # sidebar
        self.container.columnconfigure(1, weight=1)  # main content

        self.sidebar = tk.Frame(self.container, bg="#272727")
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content_frame = tk.Frame(self.container, bg="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=1)

        # Carica immagini (generiche, puoi cambiarne il percorso)
        self.welcome_img = PhotoImage(file="assets/icons/welcome.png")
        self.welcome_hover = PhotoImage(file="assets/icons/welcome_hover.png")

        self.notes_img = PhotoImage(file="assets/icons/notes.png")
        self.notes_hover = PhotoImage(file="assets/icons/notes_hover.png")

        #self.calendar_img = PhotoImage(file="assets/calendar.png")
        #self.calendar_hover = PhotoImage(file="assets/calendar_hover.png")

        # Crea i bottoni con immagine e hover
        self.welcome_button = tk.Button(self.sidebar, image=self.welcome_img, bg="#272727", borderwidth=0,
                                        highlightthickness=0, relief="flat", activebackground="#272727",
                                        command=self.show_welcome)
        self.welcome_button.pack(pady=20)
        self.welcome_button.bind("<Enter>", lambda e: self.welcome_button.config(image=self.welcome_hover))
        self.welcome_button.bind("<Leave>", lambda e: self.welcome_button.config(image=self.welcome_img))

        self.notes_button = tk.Button(self.sidebar, image=self.notes_img, bg="#272727", borderwidth=0,
                                      highlightthickness=0, relief="flat", activebackground="#272727",
                                      command=self.show_list)
        self.notes_button.pack(pady=20)
        self.notes_button.bind("<Enter>", lambda e: self.notes_button.config(image=self.notes_hover))
        self.notes_button.bind("<Leave>", lambda e: self.notes_button.config(image=self.notes_img))

        #self.calendar_button = tk.Button(self.sidebar, image=self.calendar_img, bg="#272727", borderwidth=0,
                                         #highlightthickness=0, relief="flat", activebackground="#272727",
                                         #command=self.show_calendar)
        #self.calendar_button.pack(pady=20)
        #self.calendar_button.bind("<Enter>", lambda e: self.calendar_button.config(image=self.calendar_hover))
        #self.calendar_button.bind("<Leave>", lambda e: self.calendar_button.config(image=self.calendar_img))


        self.welcome_view = WelcomeView(self.content_frame)
        self.notes_view = NotesView(self.content_frame)
        self.notes_list_view = NotesListView(self.content_frame)
        self.notes_list_view.set_note_loader(self.load_note_into_editor)

        self.show_welcome()

    def show_welcome(self):
        self.notes_view.frame.grid_forget()
        self.notes_list_view.frame.grid_forget()
        self.welcome_view.frame.grid(row=0, column=0, sticky="nsew")

    def show_notes(self):
        self.notes_list_view.frame.grid_forget()
        self.notes_view.frame.grid(row=0, column=0, sticky="nsew")

    def show_list(self):
        self.notes_view.frame.grid_forget()
        self.notes_list_view.refresh()
        self.notes_list_view.frame.grid(row=0, column=0, sticky="nsew")

    def load_note_into_editor(self, note_data):
        self.show_notes()
        if note_data:
            self.notes_view.load_note(note_data)
        else:
            self.notes_view.clear_editor()
