import tkinter as tk
from tkinter import ttk
import subprocess


class AgendaApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        aff_frame = ttk.Frame(self)
        aff_frame.pack(side="top", fill="both", expand=True)
        afficher_button = ttk.Button(aff_frame, text="Afficher le calendrier",style='secondary', command=self.open_calendar)
        afficher_button.pack(side="bottom", padx=50, pady=50)

    def open_calendar(self):
        subprocess.Popen(["python", "test.py"])
