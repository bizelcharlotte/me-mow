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
        """
        A description of the entire function, its parameters, and its return types.
        """
        return str(self.id_)

    @staticmethod
    def empty() -> 'Date':
        """
        A static method that creates and returns an empty Date object with default values for id_, date, taille, and poids.
        Returns:
            Date: An empty Date object.
        """
        return Date(
            id_=-1,
            date='',
            taille='',
            poids='',

        )

    @classmethod
    def from_row(cls, cursor: Cursor, row: Row) -> 'Date':
        """
        A description of the entire function, its parameters, and its return types.
        """
        return cls(
            id_=row[0],
            date=row[1],
            taille=row[2],
            poids=row[3],
        )


class DateStore:
    def __init__(self, path: Path):
        """
        Initialize the object with the provided path.

        :param path: Path: The path to the database.
        :return: None
        """
        self.conn: Connection = connect(path)
        self.conn.row_factory = Date.from_row

    def create_table(self):
        """
        Create a table in the database if it does not already exist.

        This function executes a SQL query to create a table named t_Dates with specific columns if it does not exist in the database.
        If the table is successfully created, the changes are committed to the database.
        If an error occurs during the execution of the query, an exception is raised with the specific error message.
        """
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
        """
        Update a date entry in the t_Dates table.

        Parameters:
            old_date (Date): The old date object to be updated.
            new_date (Date): The new date object with updated information.

        Returns:
            None
        """
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
        """
        A function that deletes a record from the t_Dates table based on the provided date's id.

        Parameters:
            date (Date): The Date object containing the id of the record to be deleted.

        Raises:
            Exception: If there is an error during the deletion process.

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
        A method to list dates from the database table t_Dates.
        Returns a list of Date objects.
        """
        sql_query = """SELECT * FROM t_Dates;"""

        try:
            result: Cursor = self.conn.execute(sql_query)
            return result.fetchall()

        except Error:
            raise Exception(f"error listing dates:{sql_query}") from Error

    def get_date(self, id_: int) -> Date:  # de base (self,id:int)
        """
        Get a date from the database based on the given ID.

        Parameters:
        - id_ (int): The ID of the date to retrieve.

        Returns:
        - Date: The date information fetched from the database.
        """
        sql_query = """SELECT * FROM t_Dates WHERE id = ?;"""

        try:
            result: Cursor = self.conn.execute(sql_query, [id_])
            return result.fetchone()
        except Error:
            raise Exception(f"error getting date {id_}")from Error

    def insert_date(self, date: Date):
        """
        Insert a Date object into the database table t_Dates.

        Parameters:
            date (Date): The Date object to be inserted.

        Returns:
            Date: The Date object with the id assigned from the database after insertion.
        """
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
        """
        Closes the connection.
        """
        self.conn.close()
