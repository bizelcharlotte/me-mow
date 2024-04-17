import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt

# Fonction pour ajouter les données dans la base de données
def add_data():
    weight = entry_weight.get()
    height = entry_height.get()

    try:
        weight = float(weight)
        height = float(height)

        # Connexion à la base de données
        conn = sqlite3.connect('weight_height_data.db')
        c = conn.cursor()

        # Création de la table si elle n'existe pas encore
        c.execute('''CREATE TABLE IF NOT EXISTS weight_height
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, weight REAL, height REAL)''')

        # Insertion des données
        c.execute("INSERT INTO weight_height (weight, height) VALUES (?, ?)", (weight, height))
        conn.commit()

        # Fermeture de la connexion
        conn.close()

        messagebox.showinfo('Success', 'Data added successfully.')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter numerical values.')

# Fonction pour supprimer les données de la base de données
def delete_data():
    try:
        selected_item = treeview.selection()[0]
        item_id = treeview.item(selected_item)['values'][0]

        # Connexion à la base de données
        conn = sqlite3.connect('weight_height_data.db')
        c = conn.cursor()

        # Suppression des données
        c.execute("DELETE FROM weight_height WHERE id=?", (item_id,))
        conn.commit()

        # Mise à jour de l'affichage
        treeview.delete(selected_item)

        # Fermeture de la connexion
        conn.close()

        messagebox.showinfo('Success', 'Data deleted successfully.')
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a data item to delete.')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {e}')

# Fonction pour afficher le graphique
def show_graph():
    # Connexion à la base de données
    conn = sqlite3.connect('weight_height_data.db')
    c = conn.cursor()

    # Récupération des données
    c.execute("SELECT weight, height FROM weight_height")
    data = c.fetchall()

    if len(data) == 0:
        messagebox.showwarning('Warning', 'No data found.')
        return

    weights, heights = zip(*data)

    # Tracé du graphique
    plt.figure(figsize=(8, 6))
    plt.scatter(heights, weights)
    plt.xlabel('Taille (m)')
    plt.ylabel('Poids (kg)')
    plt.title('graphique taille et poids')
    plt.grid(True)
    plt.show()

    # Fermeture de la connexion
    conn.close()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Weight vs Height Data")

# Cadre pour les champs d'entrée
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10)

label_weight = ttk.Label(input_frame, text="Weight (kg):")
label_weight.grid(row=0, column=0, padx=5, pady=5, sticky='w')

entry_weight = ttk.Entry(input_frame)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

label_height = ttk.Label(input_frame, text="Height (m):")
label_height.grid(row=1, column=0, padx=5, pady=5, sticky='w')

entry_height = ttk.Entry(input_frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Boutons pour ajouter, supprimer et afficher le graphique
button_frame = ttk.Frame(root)
button_frame.pack(padx=10, pady=10)

add_button = ttk.Button(button_frame, text="Add Data", command=add_data)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = ttk.Button(button_frame, text="Delete Data", command=delete_data)
delete_button.grid(row=0, column=1, padx=5, pady=5)

show_graph_button = ttk.Button(button_frame, text="Show Graph", command=show_graph)
show_graph_button.grid(row=0, column=2, padx=5, pady=5)

# Affichage des données dans un arbre
tree_frame = ttk.Frame(root)
tree_frame.pack(padx=10, pady=10)

treeview = ttk.Treeview(tree_frame, columns=("ID", "Weight", "Height"), show="headings")
treeview.heading("ID", text="ID")
treeview.heading("Weight", text="Weight (kg)")
treeview.heading("Height", text="Height (m)")
treeview.pack(side="left")

# Connexion à la base de données
conn = sqlite3.connect('weight_height_data.db')
c = conn.cursor()

# Récupération des données
c.execute("SELECT * FROM weight_height")
data = c.fetchall()

# Affichage des données dans l'arbre
for row in data:
    treeview.insert("", "end", values=row)

# Fermeture de la connexion
conn.close()

root.mainloop()
