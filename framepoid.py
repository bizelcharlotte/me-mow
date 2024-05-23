import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from pathlib import Path
from tpdata import DateStore, Date
from ttkbootstrap.dialogs import Messagebox

class FramePoids(ttk.Frame):
    def __init__(self, parent):
        """
        Initialize the class with a parent widget.
        """
        super().__init__(parent)
        self.dates: DateStore = DateStore(Path('tpdata.db'))
        self.__make_frame_left()
        self.__make_frame_center()
        self.__make_frame_right()
        self.__make_frame_bottom()
        self.dates.create_table()
        for date in self.dates.list_dates():
            self.tree.insert('', ttk.END, values=(date.iid, date.id_, date.date, date.taille, date.poids,))

    @staticmethod
    def showerror(message: str):
        """
        A static method to display an error message using Messagebox.

        Parameters:
            message (str): The error message to be displayed.

        Returns:
            None
        """
        Messagebox.show_error(message, title="error")

    def __make_frame_left(self):
        """
        Function to create and pack buttons in the left frame of the GUI.
        """
        frame_left = ttk.Frame(self, borderwidth=2)
        frame_left.pack(side=ttk.LEFT, fill=ttk.Y, expand=ttk.YES)

        btn_create = ttk.Button(frame_left, text='create', style='secondary', command=self.create)
        btn_create.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

        btn_save = ttk.Button(frame_left, text='save', style='secondary', command=self.save)
        btn_save.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

        btn_mod = ttk.Button(frame_left, text='modify', style='secondary', command=self.update)
        btn_mod.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

        btn_del = ttk.Button(frame_left, text='delete', style='secondary', command=self.delete)
        btn_del.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

        btn_quit = ttk.Button(frame_left, text='quiter application', style='secondary', command=self.quit)
        btn_quit.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

    def __make_frame_center(self):
        """
        Function to create a frame at the center of the widget with various labels and Entry widgets for date, taille, and poids data input.
        """
        frame_center = ttk.Frame(self, borderwidth=30)
        frame_center.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.NO)

        self.__sv_date = ttk.StringVar()
        self.__sv_taille = ttk.StringVar()
        self.__sv_poids = ttk.StringVar()

        ent_date = ttk.Entry(frame_center, textvariable=self.__sv_date)
        ent_taille = ttk.Entry(frame_center, textvariable=self.__sv_taille)
        ent_poids = ttk.Entry(frame_center, textvariable=self.__sv_poids)

        ent_date.grid(row=0, column=1, sticky=ttk.EW)
        ent_taille.grid(row=1, column=1, sticky=ttk.EW)
        ent_poids.grid(row=2, column=1, sticky=ttk.EW)

        date_label = ttk.Label(frame_center, text='date :')
        date_label.grid(row=0, column=0)

        taille_label = ttk.Label(frame_center, text='taille:')
        taille_label.grid(row=1, column=0)

        poids_label = ttk.Label(frame_center, text='poids:')
        poids_label.grid(row=2, column=0)

    def __make_frame_right(self):
        """
        Generates the right frame for the GUI, containing a Treeview widget to display data.
        """
        frame_right = ttk.Frame(self, borderwidth=20)
        frame_right.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.tree = ttk.Treeview(frame_right, columns=('iid', 'id', 'date', 'taille', 'poids'), show=ttk.HEADINGS,
                                 selectmode=ttk.BROWSE,
                                 displaycolumns=('date', 'taille', 'poids'))

        self.tree.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.tree.column('date', width=100, stretch=ttk.YES,anchor=ttk.CENTER)
        self.tree.column('taille', width=100, stretch=ttk.YES,anchor=ttk.CENTER)
        self.tree.column('poids', width=100, stretch=ttk.YES,anchor=ttk.CENTER)

        self.tree.heading('date', text='date')
        self.tree.heading('taille', text='taille')
        self.tree.heading('poids', text='poids')

        y_scroller = ttk.Scrollbar(frame_right, orient=ttk.VERTICAL, command=self.tree.yview)
        y_scroller.pack(side=ttk.RIGHT, fill=ttk.Y)

        self.tree.configure(yscrollcommand=y_scroller.set)
        y_scroller.pack(side=ttk.RIGHT, fill=ttk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.select)

    def __make_frame_bottom(self):
        """
        Creates and configures the bottom frame of the UI with two buttons for different graphs.
        """
        frame_bottom = ttk.Frame(self, borderwidth=2)
        frame_bottom.pack(side=ttk.BOTTOM, fill=ttk.X, expand=ttk.YES)

        btn_graph1 = ttk.Button(frame_bottom, text='Graphique Taille/Date', style='primary',
                                command=self.size_graph)
        btn_graph1.pack(side=ttk.LEFT, fill=ttk.X, padx=10, pady=10)

        btn_graph2 = ttk.Button(frame_bottom, text='Graphique Poids/Date', style='primary',
                                command=self.weight_graph)
        btn_graph2.pack(side=ttk.LEFT, fill=ttk.X, padx=10, pady=10)

    def size_graph(self):
        """
        Generate a graph showing the relationship between dates and sizes of the items in the tree.
        """
        dates = []
        sizes = []

        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            dates.append(values[2])  # Assuming 'date' is at index 2
            sizes.append(float(values[3]))  # Assuming 'taille' is at index 3

        plt.plot(dates, sizes, 'bo-')
        plt.xlabel('Date')
        plt.ylabel('Taille')
        plt.title('graphique de la taille avec les dates')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

    def weight_graph(self):
        """
        Generate a weight graph based on the data stored in the tree.
        """
        dates = []
        weights = []

        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            dates.append(values[2])  # Assuming 'date' is at index 2
            weights.append(float(values[4]))  # Assuming 'poids' is at index 4

        plt.plot(dates, weights, 'ro-')
        plt.xlabel('Date')
        plt.ylabel('Poids')
        plt.title('graphique du poids avec les dates')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

    def create(self):
        """
        Method to create something.
        """
        self.__sv_date.set('')
        self.__sv_taille.set('')
        self.__sv_poids.set('')

    def save(self):
        """
        Save the data by creating a new Date object with the provided attributes and inserting it into the database.
        If successful, update the tree view with the new date information.
        If an exception occurs during the process, display the error message.
        """
        date = Date(id_=-1,
                    date=self.__sv_date.get(),
                    poids=self.__sv_taille.get(),
                    taille=self.__sv_poids.get()
                    )

        try:
            date = self.dates.insert_date(date)
            self.tree.insert("", "end", values=(date.iid, date.id, date.date, date.taille, date.poids))
        except Exception as e:

            self.showerror(message=str(e))

    def update(self):
        """
        Update the selected item in the tree view with new date information.

        Parameters:
            None

        Returns:
            None
        """
        selection = self.tree.selection()
        item = self.tree.item(selection, option='values')
        id_ = int(item[1])

        try:

            old_date = self.dates.get_date(id_)
            new_date = Date(id_=old_date.id_,
                            date=self.__sv_date.get(),
                            taille=self.__sv_taille.get(),
                            poids=self.__sv_poids.get(),

                            )

            self.dates.update_date(old_date, new_date)
            self.tree.delete(selection)
            self.tree.insert("", "end", values=(new_date.iid, new_date.id_, new_date.date, new_date.note))

        except Exception as e:

            self.showerror(message=str(e))

    def delete(self):
        """
        Delete the selected item from the treeview, including its associated date entry.
        """
        selection = self.tree.selection()
        item = self.tree.item(selection, option='values')
        id_ = int(item[1])
        date = self.dates.get_date(id_)
        try:

            self.dates.delete_date(date)
            self.tree.delete(selection)

        except Exception as e:

            self.showerror(message=str(e))

    def select(self, event):
        """
        Handle the selection of an item in the treeview.

        :param event: The event that triggered the selection.
        :return: None
        """
        try:
            selection = self.tree.selection()
            item = self.tree.item(selection, option='values')
            id_ = int(item[1])
        except IndexError:
            return

        try:
            date = self.dates.get_date(id_)
            self.show_date(date)
        except Exception as e:

            self.showerror(message=str(e))
        except IndexError:
            self.show_date(Date.empty())

    def show_date(self, date):
        """
        Set the provided date attributes on the corresponding internal variables.

        :param date: Date object containing date, taille, and poids attributes.
        :return: None
        """
        self.__sv_date.set(date.date)
        self.__sv_taille.set(date.taille)
        self.__sv_poids.set(date.poids)
