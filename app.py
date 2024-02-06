import ttkbootstrap as ttk
from framenote import FrameNote
from framecal import FrameCal
from framepoid import FramePoid



class App(ttk.Window):
    def __init__(self):
        super().__init__(title="Me-Mow",themename="superhero")

        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="Note")

        self.framecal = FrameCal(self.book)
        self.book.add(self.framecal, text="calendrier")

        self.framepoid = FramePoid(self.book)
        self.book.add(self.framepoid, text="poid")


if __name__ == "__main__":
    main = App()
    main.mainloop()