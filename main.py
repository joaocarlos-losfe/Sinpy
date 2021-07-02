from base_de_dados import Database

from farmacia import Farmacia

database = Database()
db_2 = Database()

print(db_2 is database)

print(db_2.total_instancias) # vai ser so uma pq ja foi instanciada antes

farmacia = Farmacia()

farmacia.abrir_farmacia()
