from remedio import Remedio
from base_de_dados import Database
class Farmacia:
    def __init__(self):
        self._estoque = {}

    def abrir_farmacia(self):

        self.db_carregar_medicamentos()

        while True:
            print('1 - cadastrar medicamento')
            print('2 - ver estoque')
            print('3 - atualizar medicamento')
            print('> ')
            op = input()

            if op == '1':
                self.cadastrar_medicamento()
            elif op == '2':
                self.mostrar_estoque()
            elif op == '3':
                pass
            else:
                print('opção invalida...')

    def cadastrar_medicamento(self):
        codigo_barras = input('codigo de barras: ')

        if codigo_barras not in self._estoque:
            nome_medicamento = input('Nome do medicamento: ')
            qtd = int(input('Quantidade: '))
            preco = float(input('Preço do medicamento: '))

            remedio = Remedio()
            remedio.set_remedio(codigo_barras, nome_medicamento, qtd, preco)

            self._estoque[codigo_barras] = remedio

        else:
            print('Medicamento já cadastrado')

    def mostrar_estoque(self):
        for medicamento in self._estoque.values():
            print(medicamento.__str__())

    def atualizar_medicamento(self):
        pass

    def db_carregar_medicamentos(self):
        db = Database()
        dados = db.get_medicamentos()

        for medicamento in dados:
            remedio = Remedio()
            remedio.set_remedio(medicamento[0], medicamento[1], medicamento[2], medicamento[3])
            self._estoque[medicamento[0]] = remedio