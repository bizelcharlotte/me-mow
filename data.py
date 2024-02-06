from dataclasses import dataclass
from pathlib import Path
from sqlite3 import connect, Row,Cursor, Connection,Error

@dataclass
class Date:

    id: int
    date: str
    note: str
   
    @property
    def iid(self)-> str:
      

        return str(self.id)
    
    @staticmethod
    def empty() -> 'Date':
    

        return Date(
            id = -1,
            date= '',
            note = '',
            
            )
    
    @classmethod
    def from_row(cls,cursor : Cursor, row : Row ) -> 'Date':
 

        return cls(
            id = row[0],
            date = row[1],
            note = row[2],
           
        )

class DateStore:
    def __init__(self,path : Path):
      

        self.conn : Connection = connect(path) 
        self.conn.row_factory = Date.from_row

    def create_table(self):

        sql_query = """CREATE TABLE IF NOT EXISTS t_Dates(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	date TEXT NOT NULL,
        note TEXT NOT NULL
);"""
 
 
        try:
                self.conn.execute(sql_query)
                self.conn.commit()
        except Error:
                raise Exception(f"error creating table {sql_query}") from Error
            

    def update_date(self,old_date : Date,new_date : Date):
     
        sql_query = """UPDATE t_Dates
                    SET date = ?,
                    note = ?,
                    WHERE id = ?
                    ;"""
        try: 
                self.conn.execute(sql_query,(
                                            new_date.date,
                                            new_date.note,
                                            old_date.id
                                            
                                            ))
                self.conn.commit()

        except Error:
                raise Exception(f"error updating Dates {old_date}") from Error

    def delete_date(self,date : Date):
     
        sql_query = """DELETE FROM t_Dates WHERE id = ?;"""
        
        try:
                self.conn.execute(sql_query,[date.id])
                self.conn.commit()
        except Error:
                raise Exception(f"error deleting website {date}")from Error
        
    def list_dates(self) -> list[Date]:
       
        
        sql_query = """SELECT * FROM t_Dates;"""
    

        try:
                result:Cursor = self.conn.execute(sql_query)                
                return result.fetchall()
            
        except Error:
                raise Exception(f"error listing dates:{sql_query}") from Error
            
    def get_date(self,id : int)-> Date:
     
        sql_query = """SELECT * FROM t_Dates WHERE id = ?;"""
        
        try:
                result:Cursor = self.conn.execute(sql_query,[id])
                return result.fetchone()
        except Error:
                raise Exception(f"error getting date {id}")from Error

    def insert_date(self,date : Date):
     
        
        sql_query = """INSERT INTO t_Dates (date,note)
                    VALUES(?,?);"""

        try:
                result = self.conn.execute(sql_query,(date.date,
                                                   date.note,
                                                   ))
                date.id = result.lastrowid
                self.conn.commit()
                return date
            
        except Error:
                raise Exception(f"error inserting date {date}") from Error
    
    def close(self):
     
        self.conn.close()