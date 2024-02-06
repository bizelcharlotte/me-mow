import ttkbootstrap as ttk
from framenote import FrameNote
class App(ttk.Window):
    def __init__(self):
        super().__init__(title="Me-Mow",themename="superhero")

        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="Note")

        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="calandrier")

        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="poid")


if __name__ == "__main__":
    main = App()
    main.mainloop()