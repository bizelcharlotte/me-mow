from dataclasses import dataclass
from pathlib import Path
from sqlite3 import connect, Row, Cursor, Connection, Error


@dataclass
class Date:
    id_: int
    date: str
    taille: str
    poids: str

    @property
    def iid(self) -> str:
        return str(self.id_)

    @staticmethod
    def empty() -> 'Date':
        return Date(
            id_=-1,
            date='',
            taille='',
            poids='',

        )

    @classmethod
    def from_row(cls, cursor: Cursor, row: Row) -> 'Date':
        return cls(
            id_=row[0],
            date=row[1],
            taille=row[2],
            poids=row[3],
        )


class DateStore:
    def __init__(self, path: Path):

        self.conn: Connection = connect(path)
        self.conn.row_factory = Date.from_row

    def create_table(self):

        sql_query = """CREATE TABLE IF NOT EXISTS t_Dates
                    (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    date TEXT NOT NULL,
                    taille TEXT NOT NULL,
                    poids TEXT NOT NULL
                        );"""

        try:
            self.conn.execute(sql_query)
            self.conn.commit()
        except Error:
            raise Exception(f"error creating table {sql_query}") from Error

    def update_date(self, old_date: Date, new_date: Date):

        sql_query = """UPDATE t_Dates
                    SET date = ?,
                    taille = ?,
                    poids = ?,
                    WHERE id = ?
                    ;"""
        try:
            self.conn.execute(sql_query, (
                new_date.date,
                new_date.taille,
                new_date.poids,
                old_date.id_

            ))
            self.conn.commit()

        except Error:
            raise Exception(f"error updating Dates {old_date}") from Error

    def delete_date(self, date: Date):

        sql_query = """DELETE FROM t_Dates WHERE id = ?;"""

        try:
            self.conn.execute(sql_query, [date.id_])
            self.conn.commit()
        except Error:
            raise Exception(f"error deleting website {date}")from Error

    def list_dates(self) -> list[Date]:

        sql_query = """SELECT * FROM t_Dates;"""

        try:
            result: Cursor = self.conn.execute(sql_query)
            return result.fetchall()

        except Error:
            raise Exception(f"error listing dates:{sql_query}") from Error

    def get_date(self, id_: int) -> Date:  # de base (self,id:int)

        sql_query = """SELECT * FROM t_Dates WHERE id = ?;"""

        try:
            result: Cursor = self.conn.execute(sql_query, [id_])
            return result.fetchone()
        except Error:
            raise Exception(f"error getting date {id_}")from Error

    def insert_date(self, date: Date):

        sql_query = """INSERT INTO t_Dates (date,taille,poids)
                    VALUES(?,?,?);"""

        try:
            result = self.conn.execute(sql_query, (date.date,
                                                   date.taille,
                                                   date.poids,
                                                   ))
            date.id = result.lastrowid
            self.conn.commit()
            return date

        except Error:
            raise Exception(f"error inserting date {date}") from Error

    def close(self):

        self.conn.close()
