import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Affichage d'une photo avec ttkbootstrap")


image_path = "pitichat.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)


label = ttk.Label(root, image=photo)
label.pack()

root.mainloop()
