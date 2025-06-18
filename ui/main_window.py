import tkinter as tk                                                 # importa la libreria tkinter
from ui.welcome_view import WelcomeView                              # importa la classe WelcomeView
from ui.notes_view import NotesView                                  # importa la classe NotesView
from ui.calendar_view import CalendarView                            # importa la classe CalendarView
from tkinter import PhotoImage                                       # importa la classe PhotoImage

class MainWindow: # Classe principale MainWindow
    # Metodi ---------------------------------------------------------------------------------------------------
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
    
    

    def __init__(self, root): # Costruttore-----------------------------------------------------------------------

        self.root = root                                             # Inizializza la finestra principale
        self.root.title("Edgar Notes: Note e Calendario")            # Imposta il titolo della finestra

        # Layout principale: sidebar + area di contenuto----------------------------------------------------------

        self.root.grid_rowconfigure(0, weight=1)                     # Configura la griglia della finestra [numero riga, peso]
        self.root.grid_columnconfigure(1, weight=1)                  # Configura la griglia della finestra [numero colonna, peso] 
                                                                     # 1 riga e 2 colonne: sidebar + area di contenuto

        self.sidebar = tk.Frame(self.root, bg="#272727", width=150)   # Crea la sidebar
        self.sidebar.grid(row=0, column=0, sticky="ns")                 # Posiziona la sidebar. La si associa alla riga 0 e alla colonna 0

        self.content_frame = tk.Frame(self.root, bg="white")            # Crea la area di contenuto
        self.content_frame.grid(row=0, column=1, sticky="nsew")         # Posiziona la area di contenuto. La si associa alla riga 0 e alla colonna 1

        # Pulsanti nella sidebar ----------------------------------------------------------------------------------

        # Carica immagini (path sostituibile. Momentaneamente su assets)

        self.welcome_img = PhotoImage(file="assets/icons/welcome.png")
        self.welcome_hover = PhotoImage(file="assets/icons/welcome_hover.png")

        self.notes_img = PhotoImage(file="assets/icons/notes.png")
        self.notes_hover = PhotoImage(file="assets//icons/notes_hover.png")

        self.calendar_img = PhotoImage(file="assets/icons/calendar.png")
        self.calendar_hover = PhotoImage(file="assets//icons/calendar_hover.png")

        # Crea i bottoni con immagine e hover

        # Home button
        self.welcome_button = tk.Button(self.sidebar, image=self.welcome_img, bg="#272727", borderwidth=0, highlightthickness=0, relief="flat", 
                                        activebackground="#272727",command=self.show_welcome)
        self.welcome_button.pack(pady=20) # posiziona il pulsante
        self.welcome_button.bind("<Enter>", lambda e: self.welcome_button.config(image=self.welcome_hover)) # al passaggio del mouse
        self.welcome_button.bind("<Leave>", lambda e: self.welcome_button.config(image=self.welcome_img))   # al ritorno del mouse
        
        # Notes button
        self.notes_button = tk.Button(self.sidebar, image=self.notes_img, bg="#272727", borderwidth=0, highlightthickness=0, relief="flat", 
                                      activebackground="#272727",command=self.show_notes)
        self.notes_button.pack(pady=20)
        self.notes_button.bind("<Enter>", lambda e: self.notes_button.config(image=self.notes_hover))
        self.notes_button.bind("<Leave>", lambda e: self.notes_button.config(image=self.notes_img))

        # Calendar button
        self.calendar_button = tk.Button(self.sidebar, image=self.calendar_img, bg="#272727", borderwidth=0, highlightthickness=0, relief="flat", 
                                         activebackground="#272727",command=self.show_calendar)
        self.calendar_button.pack(pady=20)
        self.calendar_button.bind("<Enter>", lambda e: self.calendar_button.config(image=self.calendar_hover))
        self.calendar_button.bind("<Leave>", lambda e: self.calendar_button.config(image=self.calendar_img))


        # Inizializza viste -----------------------------------------------------------------------------------------

        self.welcome_view = WelcomeView(self.content_frame)     # Inizializza la vista di benvenuto
        self.notes_view = NotesView(self.content_frame)         # Inizializza la vista note
        self.calendar_view = CalendarView(self.content_frame)   # Inizializza la vista calendario

        # Mostra per default la vista note
        self.show_welcome()

    