import os
import pathlib
import sqlite3

class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instancias:
            instance = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instance
        return cls._instancias[cls]


class Query:
    @staticmethod
    def query_criar_tabela():
        return """
                    CREATE TABLE IF NOT EXISTS Medicamentos
                    (
                        codigo_de_barras VARCHAR(15) NOT NULL PRIMARY KEY,
                        nome VARCHAR(50) NOT NULL,
                        qtd INTEGER NOT NULL,
                        preco REAL NOT NULL
                    );
                    """

    @staticmethod
    def query_salvar():
        return  """
                INSERT INTO Medicamentos (codigo_de_barras, nome,  qtd, preco)
                VALUES (?, ?, ?, ?)
                """

    @staticmethod
    def query_atualizar(self):
        return  """
                UPDATE Medicamentos
                SET qtd = ?, nome = ?
                WHERE codigo_de_barras = ?;
                """
    @staticmethod
    def query_delete(self):
        return  """
                DELETE FROM Medicamentos WHERE codigo_de_barras = ?
                """

    @staticmethod
    def query_obter_dados():
        return  """
                    SELECT * FROM Medicamentos
                """

class Database(Query, metaclass=SingletonMeta):

    total_instancias = 0

    def __init__(self):

        self._db_path = pathlib.Path(__file__).parent.absolute()
        self._db_path = os.path.join(self._db_path, "arquivo_db.db")
        Database.total_instancias +=1

        if not os.path.isfile(self.get_db_path):
            conn = sqlite3.connect(self.get_db_path)
            exec = conn.cursor()
            exec.execute(super().query_criar_tabela())

    @property
    def get_db_path(self):
        return self._db_path

    def get_medicamentos(self):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_obter_dados())

        dados = []

        for medicamento in exec.fetchall():
            dados.append(medicamento)

        return dados

    def salvar(self, codigo_barras, nome, qtd, preco):
        conn = sqlite3.connect(self.get_db_path)
        exec = conn.cursor()
        exec.execute(super().query_salvar(), (codigo_barras, nome, qtd, preco, ))
        conn.commit()

    def atualizar(self):
        pass

    def deletar(self, task_id):
        pass