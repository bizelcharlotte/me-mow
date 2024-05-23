import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter.simpledialog as sd
import json
import locale


class AgendaApp(tk.Tk):
    def __init__(self):
        """
        Initialize the Agenda class with tasks loaded from a JSON file, a calendar in French locale, and buttons for adding, deleting, and modifying tasks.
        """
        super().__init__()

        self.title("Agenda")

        self.tasks_file = "tasks.json"  # Fichier pour stocker les tâches

        # Charger les tâches depuis le fichier
        try:
            with open(self.tasks_file, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = {}

        self.calendar_frame = ttk.Frame(self)
        self.calendar_frame.pack(side="left", fill="both", expand=True)

        # Set en fancais
        locale.setlocale(locale.LC_TIME, "fr_FR.utf8")

        self.calendar = Calendar(self.calendar_frame, selectmode="day", date_pattern="dd/MM/yyyy",locale="fr_FR")
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
        """
        A function to display tasks for a selected date.
        """
        selected_date = self.calendar.get_date()

        self.tasks_listbox.delete(0, tk.END)
        tasks_for_date = self.tasks.get(selected_date, [])
        for task in tasks_for_date:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):
        """
        save task in file JSON
        """

        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f)

    def add_task(self):
        """
        add a new task
        """
        selected_date = self.calendar.get_date()
        new_task = sd.askstring("Ajouter une tâche", "Entrez le nom de la nouvelle tâche:")
        if new_task:
            if selected_date in self.tasks:
                self.tasks[selected_date].append(new_task)
            else:
                self.tasks[selected_date] = [new_task]
            self.save_tasks()
            self.show_tasks()

    def delete_task(self):
        """
      delete a task
        """
        selected_date = self.calendar.get_date()
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            del self.tasks[selected_date][selected_index[0]]
            if not self.tasks[selected_date]:
                del self.tasks[selected_date]
            self.save_tasks()
            self.show_tasks()

    def modify_task(self):
        """
        Modifier une tâche
        """
        selected_date = self.calendar.get_date()
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            modified_task = sd.askstring("Modifier une tâche", "Entrez le nouveau nom de la tâche:")
            if modified_task:
                self.tasks[selected_date][selected_index[0]] = modified_task
                self.save_tasks()
                self.show_tasks()


if __name__ == "__main__":
    app = AgendaApp()
    app.mainloop()
