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
    
    def make_center_frame():
        pass

    def make_right_frame():
        pass