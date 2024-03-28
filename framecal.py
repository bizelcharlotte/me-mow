import ttkbootstrap as ttk
class FrameCal(ttk.Frame):
     def __init__(self,parent):
        super().__init__(parent)
            
        frame_left = ttk.Frame(self, borderwidth=2)
        frame_left.pack(side=ttk.LEFT, fill=ttk.Y, expand=ttk.YES)
    
        btn_create = ttk.Button(frame_left, text='create', bootstyle='secondary')
        btn_create.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_save = ttk.Button(frame_left, text='save',bootstyle='secondary')
        btn_save.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_mod = ttk.Button(frame_left, text='modify', bootstyle='secondary')
        btn_mod.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_del = ttk.Button(frame_left, text='delete', bootstyle='secondary')
        btn_del.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)

        btn_quit = ttk.Button(frame_left, text='quit', bootstyle='secondary')
        btn_quit.pack(side=ttk.TOP,fill=ttk.X, padx=10, pady=10)
    
