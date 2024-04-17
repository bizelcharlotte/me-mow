import sqlite3

class PoidData:
    def __init__(self):
        self.conn = sqlite3.connect('weight_data.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS weight_data
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, weight REAL, date TEXT)''')
        self.conn.commit()

    def add_data(self, weight, date):
        self.c.execute("INSERT INTO weight_data (weight, date) VALUES (?, ?)", (weight, date))
        self.conn.commit()

    def delete_data(self, id):
        self.c.execute("DELETE FROM weight_data WHERE id=?", (id,))
        self.conn.commit()

    def get_all_data(self):
        self.c.execute("SELECT * FROM weight_data")
        return self.c.fetchall()

    def close_connection(self):
        self.conn.close()
