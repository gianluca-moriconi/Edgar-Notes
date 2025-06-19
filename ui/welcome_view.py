import tkinter as tk

class WelcomeView:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="white")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        content = tk.Frame(self.frame, bg="white")
        content.grid(row=0, column=0)

        # Logo PNG semplice da path relativo
        self.logo_img = tk.PhotoImage(file="assets/icons/logo_edgar.png")
        logo_label = tk.Label(content, image=self.logo_img, bg="white")
        logo_label.pack(pady=(0, 20))

        desc_label = tk.Label(
            content,
            text="Benvenuto nell'app di note!\nOrganizza e salva i tuoi appunti con semplicità.",
            font=("Arial", 14),
            bg="white",
            fg="#34495e",
            justify="center"
        )
        desc_label.pack()
