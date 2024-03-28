import ttkbootstrap as ttk
from framenote import FrameNote
from framecal import FrameCal
from framepoid import FramePoid
from framebook import FrameBook

class App(ttk.Window):
    def __init__(self):
        super().__init__(title="Me-Mow",themename="darkly")

        frame_up = ttk.Frame(self, borderwidth=2)
        frame_up.pack(side=ttk. TOP, fill=ttk.Y, expand=ttk.YES)

        btn_open = ttk.Button(frame_up, text='photo', bootstyle='secondary')
        btn_open.pack(side=ttk.LEFT,fill=ttk.X, padx=10, pady=10,ipady=50, ipadx=50)

        label = ttk.Label(frame_up, text="Bienvenue sur Me-Mow")
        label.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES, padx=10, pady=10)

        label = ttk.Label(frame_up, text="                                                                                                                            ")
        label.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES, padx=10, pady=10)

        frame_bottom = ttk.Frame(self, borderwidth=2)
        frame_bottom.pack(side=ttk.BOTTOM, fill=ttk.Y, expand=ttk.YES)
        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="Notes")

        self.framecal = FrameCal(self.book)
        self.book.add(self.framecal, text="calendrier")

        self.framepoid = FramePoid(self.book)
        self.book.add(self.framepoid, text="poids et taille")

if __name__ == "__main__":
    main = App()
    main.mainloop()