from dataclasses import dataclass
from pathlib import Path
from sqlite3 import connect, Row, Cursor, Connection, Error


@dataclass
class Date:
    id_: int
    date: str
    note: str

    @property
    def iid(self) -> str:
        """
        Get the iid property as a string.
        """
        return str(self.id_)

    @staticmethod
    def empty() -> 'Date':
        """
        A static method that creates and returns a Date instance with default empty values.
        Returns:
            Date: A Date instance with id=-1, date='', and note=''.
        """
        return Date(
            id_=-1,
            date='',
            note='',

        )

    @classmethod
    def from_row(cls, cursor: Cursor, row: Row) -> 'Date':
        """
        A class method that creates a Date object from a database row.

        Parameters:
            cls: the class itself
            cursor: a Cursor object for database operations
            row: a Row object representing a database row

        Returns:
            Date: a Date object created from the database row
        """
        return cls(
            id_=row[0],
            date=row[1],
            note=row[2],
        )


class DateStore:
    def __init__(self, path: Path):
        """
        Initialize the object with a given path.

        Parameters:
            path (Path): The path to the file to connect to.

        Returns:
            None
        """

        self.conn: Connection = connect(path)
        self.conn.row_factory = Date.from_row

    def create_table(self):
        """
        Create a table in the database if it doesn't already exist.
        """
        sql_query = """CREATE TABLE IF NOT EXISTS t_Dates
                    (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    date TEXT NOT NULL,
                        note TEXT NOT NULL
                        );"""

        try:
            self.conn.execute(sql_query)
            self.conn.commit()
        except Error:
            raise Exception(f"error creating table {sql_query}") from Error

    def update_date(self, old_date: Date, new_date: Date):
        """
        Update a date entry in the database.

        Parameters:
            old_date (Date): The old date entry to be updated.
            new_date (Date): The new date entry with updated information.

        Raises:
            Exception: If there is an error updating the database entry.

        Returns:
            None
        """

        sql_query = """UPDATE t_Dates
                    SET date = ?,
                    note = ?,
                    WHERE id = ?
                    ;"""
        try:
            self.conn.execute(sql_query, (
                new_date.date,
                new_date.note,
                old_date.id_

            ))
            self.conn.commit()

        except Error:
            raise Exception(f"error updating Dates {old_date}") from Error

    def delete_date(self, date: Date):
        """
        A function to delete a specific date entry in the database.

        Parameters:
        date (Date): The Date object to be deleted from the database.

        Returns:
        None
        """
        sql_query = """DELETE FROM t_Dates WHERE id = ?;"""

        try:
            self.conn.execute(sql_query, [date.id_])
            self.conn.commit()
        except Error:
            raise Exception(f"error deleting website {date}")from Error

    def list_dates(self) -> list[Date]:
        """
        A function that lists dates from the database and returns them.
        """
        sql_query = """SELECT * FROM t_Dates;"""

        try:
            result: Cursor = self.conn.execute(sql_query)
            return result.fetchall()

        except Error:
            raise Exception(f"error listing dates:{sql_query}") from Error

    def get_date(self, id_: int) -> Date:  # de base (self,id:int)
        """
        Get a date by id from the database.

        Parameters:
            id_ (int): The id of the date to retrieve.

        Returns:
            Date: The date information fetched from the database.
        """
        sql_query = """SELECT * FROM t_Dates WHERE id = ?;"""

        try:
            result: Cursor = self.conn.execute(sql_query, [id_])
            return result.fetchone()
        except Error:
            raise Exception(f"error getting date {id_}")from Error

    def insert_date(self, date: Date):
        """
        Insert a new date record into the t_Dates table in the database.

        Parameters:
            date (Date): The Date object to be inserted into the database.

        Returns:
            Date: The Date object with the inserted record's ID.
        """
        sql_query = """INSERT INTO t_Dates (date,note)
                    VALUES(?,?);"""

        try:
            result = self.conn.execute(sql_query, (date.date,
                                                   date.note,
                                                   ))
            date.id = result.lastrowid
            self.conn.commit()
            return date

        except Error:
            raise Exception(f"error inserting date {date}") from Error

    def close(self):
        """
        Close the connection.
        """
        self.conn.close()
