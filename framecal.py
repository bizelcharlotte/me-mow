import tkinter as tk
from tkinter import ttk
from test import AgendaApp

class AgendaApp(tk.Frame):
    def __init__(self):
        super().__init__()

        aff_frame = ttk.Frame(self)
        aff_frame.pack(side="top", fill="both", expand=True)
        afficher_button = ttk.Button(aff_frame, text="Modifier")
        afficher_button.pack(side="left", padx=10, pady=5)

    def butt_afficher(self):
        pass




