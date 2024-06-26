import ttkbootstrap as ttk
from PIL import ImageTk, Image
from framenote import FrameNote
from framecal import AgendaApp
from framepoid import FramePoids

class App(ttk.Window):
    """
    Initialize the Me-Mow application with a dark theme.
    This function sets up the main frame and widgets for the application, including an image, labels, and a notebook with different tabs for notes, calendar, and weight/height.
    """
    def __init__(self):
        """
        Initialize the GUI for the Me-Mow application.
        """
        super().__init__(title="Me-Mow", themename="darkly")
        self.frame_up = ttk.Frame(self, borderwidth=2)
        self.frame_up.pack(side=ttk.TOP, fill=ttk.Y, expand=ttk.YES)

        image = Image.open("pitichat-modified-removebg-preview.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        self.label_image = ttk.Label(self.frame_up, image=photo)
        self.label_image.image = photo
        self.label_image.pack(side=ttk.LEFT, padx=10, pady=10)

        label = ttk.Label(self.frame_up, text="Bienvenue sur Me-Mow")
        label.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES, padx=10, pady=10)

        self.book = ttk.Notebook(self)
        self.book.pack()

        self.framenote = FrameNote(self.book)
        self.book.add(self.framenote, text="Notes")

        self.framecal = AgendaApp()
        self.book.add(self.framecal, text="Calendrier")

        self.framepoid = FramePoids(self.book)
        self.book.add(self.framepoid, text="poids et taille")


if __name__ == "__main__":
    main = App()
    main.mainloop()
