import tkinter as tk
from tkinter import ttk
import subprocess


class AgendaApp(tk.Frame):
    def __init__(self, master=None):
        """
        Constructor for the class, initializes the master widget.

        Parameters:
            master: the parent widget (default is None)

        Returns:
            None
        """
        super().__init__(master)

        self.master = master

        aff_frame = ttk.Frame(self)
        aff_frame.pack(side="top", fill="both", expand=True)
        afficher_button = ttk.Button(aff_frame, text="Afficher le calendrier",style='secondary', command=self.open_calendar)
        afficher_button.pack(padx=50, pady=50)
        btn_quit = ttk.Button(aff_frame, text='quiter application', style='secondary', command=self.quit)
        btn_quit.pack(padx=10, pady=10)

    def open_calendar(self):
        """
        Open the calendar by executing the 'test.py' script using subprocess.Popen.
        """
        subprocess.Popen(["python", "test.py"])
