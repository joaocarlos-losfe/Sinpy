import os
import pathlib
import sqlite3

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Query:
    @staticmethod
    def query_criar_tabela():
        return """
                    CREATE TABLE IF NOT EXISTS Task
                    (
                        task_id VARCHAR(15) NOT NULL PRIMARY KEY,
                        project_id VARCHAR(60) NOT NULL,
                        creation_date VARCHAR(30) NOT NULL, 
                        move_date VARCHAR(30),
                        stage VARCHAR(20) NOT NULL, 
                        text TEXT NOT NULL
                    );
                    """

    @staticmethod
    def query_salvar():
        return  """
                INSERT INTO Task (task_id, project_id, creation_date, move_date, stage, text)
                VALUES (?, ?, ?, ?, ?, ?)
                """

    @staticmethod
    def query_atualizar(self):
        return  """
                UPDATE Task
                SET move_date = ?, stage = ?, text = ?
                WHERE task_id = ?;
                """
    @staticmethod
    def query_delete(self):
        return  """
                DELETE FROM Task WHERE task_id = ?
                """

    @staticmethod
    def query_obter_dados():
        return  """
                    SELECT * FROM Task WHERE project_id = ?
                """

class Database(Query, metaclass=SingletonMeta):

    total_instancias = 0

    def __init__(self):

        self._db_path = pathlib.Path(__file__).parent.absolute()
        self._db_path = os.path.join(self._db_path, "DB")
        Database.total_instancias +=1

        if not os.path.isfile(self.get_db_path):
            conn = sqlite3.connect(self.get_db_path)
            exec = conn.cursor()
            exec.execute(super().query_criar_tabela())

    @property
    def get_db_path(self):
        return self._db_path + "local.db"

    def get_tasks(self, project_id):
        pass

    def save(self):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        conn.commit()

    def update(self):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        #exec.execute(super().query_update_data(), (move_date, stage, text, task_id, ))
        conn.commit()

    def delete(self, task_id):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        conn.commit()