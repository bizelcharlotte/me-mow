import ttkbootstrap as ttk


class FrameNote(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
            
        frame_left = ttk.Frame(self, borderwidth=2)
        frame_left.pack(side=ttk.LEFT, fill=ttk.Y, expand=ttk.YES)
    
        btn_create = ttk.Button(frame_left, text='create', style='info.TButton')
        btn_create.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_save = ttk.Button(frame_left, text='save', style='info.TButton')
        btn_save.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_mod = ttk.Button(frame_left, text='modify', style='info.TButton')
        btn_mod.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_del = ttk.Button(frame_left, text='delete', style='info.TButton')
        btn_del.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_quit = ttk.Button(frame_left, text='quit', style='light.TButton')
        btn_quit.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)
    
             
        frame_center = ttk.Frame(self, borderwidth=30)
        frame_center.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.NO)

        self.__sv_date = ttk.StringVar()
        self.__sv_note = ttk.StringVar()

        ent_date = ttk.Entry(frame_center,textvariable=self.__sv_date)
        ent_note = ttk.Entry(frame_center,textvariable=self.__sv_note)
        
        ent_date.grid(row=0, column=1,sticky=ttk.EW)
        ent_note.grid(row=1, column=1,sticky=ttk.EW)
        

        date_label = ttk.Label(frame_center, text='date :')
        date_label.grid(row=0, column=0)
        
        note_label = ttk.Label(frame_center, text='note:')
        note_label.grid(row=1, column=0)




        
        frame_right = ttk.Frame(self, borderwidth=20, relief=ttk.SUNKEN)
        frame_right.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES)

        self.tree = ttk.Treeview(frame_right,columns=('iid','id','date','note'),show= ttk.HEADINGS,
                                                        selectmode=ttk.BROWSE,
                                                        displaycolumns=('iid','id','date','note'))
        
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
        y_scroller.pack(side=ttk.RIGHT,fill=ttk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.__select)


    
    def make_center_frame():
        pass

    def make_right_frame():
        pass