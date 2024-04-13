import ttkbootstrap as ttk
from pathlib import Path
from data import DateStore, Date
from ttkbootstrap.dialogs import Messagebox


class FrameNote(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)
        self.dates: DateStore = DateStore(Path('data.db'))
        self.__make_frame_left()
        self.__make_frame_center()
        self.__make_frame_right()
        self.dates.create_table()
        for date in self.dates.list_dates():
            self.tree.insert('', ttk.END, values=(date.iid, date.id_, date.date, date.note,))

    @staticmethod
    def showerror(message: str):
        Messagebox.show_error(message, title="error")

    def __make_frame_left(self):
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

        btn_quit = ttk.Button(frame_left, text='quit', style='secondary', command=self.quit)
        btn_quit.pack(side=ttk.TOP, fill=ttk.X, padx=10, pady=10)

    def __make_frame_center(self):
        frame_center = ttk.Frame(self, borderwidth=30)
        frame_center.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.NO)

        self.__sv_date = ttk.StringVar()
        self.__sv_note = ttk.StringVar()

        ent_date = ttk.Entry(frame_center, textvariable=self.__sv_date)
        ent_note = ttk.Entry(frame_center, textvariable=self.__sv_note)

        ent_date.grid(row=0, column=1, sticky=ttk.EW)
        ent_note.grid(row=1, column=1, sticky=ttk.EW)

        date_label = ttk.Label(frame_center, text='date :')
        date_label.grid(row=0, column=0)

        note_label = ttk.Label(frame_center, text='note:')
        note_label.grid(row=1, column=0)

    def __make_frame_right(self):
        frame_right = ttk.Frame(self, borderwidth=20)
        frame_right.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES)

        self.tree = ttk.Treeview(frame_right, columns=('iid', 'id', 'date', 'note'), show=ttk.HEADINGS,
                                 selectmode=ttk.BROWSE,
                                 displaycolumns=('iid', 'id', 'date', 'note'))

        self.tree.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        self.tree.column('#0', width=0, stretch=ttk.NO)
        self.tree.column('id', width=50, stretch=ttk.YES)
        self.tree.column('date', width=100, stretch=ttk.YES)
        self.tree.column('note', width=100, stretch=ttk.YES)

        self.tree.heading('id', text='id')
        self.tree.heading('date', text='date')
        self.tree.heading('note', text='note')

        y_scroller = ttk.Scrollbar(frame_right, orient=ttk.VERTICAL, command=self.tree.yview)
        y_scroller.pack(side=ttk.RIGHT, fill=ttk.Y)

        self.tree.configure(yscrollcommand=y_scroller.set)
        y_scroller.pack(side=ttk.RIGHT, fill=ttk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.select)

    def create(self):

        self.__sv_date.set('')
        self.__sv_note.set('')

    def save(self):

        date = Date(id_=-1,
                    date=self.__sv_date.get(),
                    note=self.__sv_note.get()
                    )

        try:
            date = self.dates.insert_date(date)
            self.tree.insert("", "end", values=(date.iid, date.id, date.date, date.note))
        except Exception as e:

            self.showerror(message=str(e))

    def update(self):

        selection = self.tree.selection()
        item = self.tree.item(selection, option='values')
        id_ = int(item[1])

        try:

            old_date = self.dates.get_date(id_)
            new_date = Date(id_=old_date.id_,
                            date=self.__sv_date.get(),
                            note=self.__sv_note.get(),

                            )

            self.dates.update_date(old_date, new_date)
            self.tree.delete(selection)
            self.tree.insert("", "end", values=(new_date.iid, new_date.id_, new_date.date, new_date.note))

        except Exception as e:

            self.showerror(message=str(e))

    def delete(self):

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

        self.__sv_date.set(date.date)
        self.__sv_note.set(date.note)
