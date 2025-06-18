import tkinter as tk                                                 # importa la libreria tkinter
from ui.welcome_view import WelcomeView                              # importa la classe WelcomeView
from ui.notes_view import NotesView
from ui.calendar_view import CalendarView

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Note e Calendario")

        # Layout principale: sidebar + area di contenuto
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.sidebar = tk.Frame(self.root, bg="#272727", width=100)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # Pulsanti nella sidebar
        self.welcome_button = tk.Button(self.sidebar, bg="#272727", text="👋", font=("Arial", 18), command=self.show_welcome)
        self.welcome_button.pack(pady=20)

        self.notes_button = tk.Button(self.sidebar, bg="#272727", text="📝", font=("Arial", 18), command=self.show_notes)
        self.notes_button.pack(pady=20)

        self.calendar_button = tk.Button(self.sidebar, bg="#272727", text="📅", font=("Arial", 18), command=self.show_calendar)
        self.calendar_button.pack(pady=20)

        # Inizializza viste
        self.welcome_view = WelcomeView(self.content_frame)
        self.notes_view = NotesView(self.content_frame)
        self.calendar_view = CalendarView(self.content_frame)

        # Mostra per default la vista note
        self.show_welcome()

    def show_welcome(self):
        self.notes_view.frame.pack_forget()
        self.calendar_view.frame.pack_forget()
        self.welcome_view.frame.pack(fill="both", expand=True)

    def show_notes(self):
        self.welcome_view.frame.pack_forget()
        self.calendar_view.frame.pack_forget()
        self.notes_view.frame.pack(fill="both", expand=True)

    def show_calendar(self):
        self.welcome_view.frame.pack_forget()
        self.notes_view.frame.pack_forget()
        self.calendar_view.frame.pack(fill="both", expand=True)