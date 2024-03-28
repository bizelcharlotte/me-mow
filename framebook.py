import ttkbootstrap as ttk
from framenote import FrameNote
from framecal import FrameCal
from framepoid import FramePoid

class FrameBook(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.book = ttk.Notebook(self)
        self.book.pack()
        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="Notes")

        self.framecal = FrameCal(self.book)
        self.book.add(self.framecal, text="calendrier")

        self.framepoid = FramePoid(self.book)
        self.book.add(self.framepoid, text="poids et taille")