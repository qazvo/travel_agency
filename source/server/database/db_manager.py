import sqlite3
import os

from settings import DB_PATH

class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def connect_to_db(self) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur
    
    def check_base(self) -> bool:
        return os.path.exists(self.db_path)
    
    def create_base(self, script_tables_path: str):
        conn, cur = self.connect_to_db()
        try:
            cur.executescript(open(script_tables_path).read())
            conn.commit
            conn.close
        except sqlite3.Error as err:
            print(err)
            os.remove(self.db_path)
    
    def execute(self, query: str, args=(), many: bool = False):
        conn, cur = self.connect_to_db()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code": 200, "data": result, "inf": "OK"}
        except sqlite3.Error as err:
            return {"code": 400, "data": None, "inf" : err}
        finally:
            conn.close()
db_manager = DBManager(DB_PATH)