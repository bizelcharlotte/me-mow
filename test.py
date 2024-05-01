import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda")

        self.calendar_frame = ttk.Frame(self)
        self.calendar_frame.pack(side="left", fill="both", expand=True)

        self.calendar = Calendar(self.calendar_frame, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar.pack(fill="both", expand=True)
        self.calendar.bind("<<CalendarSelected>>", self.show_tasks)

        self.tasks_frame = ttk.Frame(self)
        self.tasks_frame.pack(side="right", fill="both", expand=True)

        self.tasks_listbox = tk.Listbox(self.tasks_frame, width=50)
        self.tasks_listbox.pack(side="top", padx=10, pady=10)

        self.add_button = ttk.Button(self.tasks_frame, text="Ajouter", command=self.add_task)
        self.add_button.pack(side="left", padx=10, pady=5)

        self.delete_button = ttk.Button(self.tasks_frame, text="Supprimer", command=self.delete_task)
        self.delete_button.pack(side="left", padx=10, pady=5)

        self.modify_button = ttk.Button(self.tasks_frame, text="Modifier", command=self.modify_task)
        self.modify_button.pack(side="left", padx=10, pady=5)

    def show_tasks(self, event=None):
        selected_date = self.calendar.get_date()
        # Ici vous devriez remplacer la logique factice par votre propre logique de récupération des tâches pour la date sélectionnée
        tasks = ["Tâche 1", "Tâche 2", "Tâche 3"]
        self.tasks_listbox.delete(0, tk.END)
        for task in tasks:
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        # Implémentez la logique pour ajouter une tâche ici
        pass

    def delete_task(self):
        # Implémentez la logique pour supprimer une tâche ici
        pass

    def modify_task(self):
        # Implémentez la logique pour modifier une tâche ici
        pass

if __name__ == "__main__":
    app = AgendaApp()
    app.mainloop()
