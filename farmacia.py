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
            print('4 - vender medicamento')
            print('> ')
            op = input()

            if op == '1':
                self.cadastrar_medicamento()
            elif op == '2':
                self.mostrar_estoque()
            elif op == '3':
                self.atualizar_medicamento()
            elif op == '4':
                self.vender_medicamento()
            else:
                print('opção invalida...')

    def atualizar_medicamento(self):

        codigo_barras = input('Codigo de barras medicamento: ')

        if codigo_barras in self._estoque:
            print(self._estoque[codigo_barras].__str__())

            if self._estoque[codigo_barras].get_qtd == 0:
                print('Atenção, esse medicamento necessita reposição...')
            else:
                print('1 - atualizar nome')
                print('2 - incrementar estoque')
                print('3 - atualizar preço')
                op = input('> ')

                if op == '1':
                    nome = input('novo nome: ')
                    self._estoque[codigo_barras].atualizar_nome(nome)
                    print('Nome atualizado...')

                elif op == '2':
                    qtd = int(input('Qtd: '))
                    self._estoque[codigo_barras].atualizar_qtd(qtd)
                    print('Quantidade atualizada...')

                elif op == '3':
                    preco = float(input('Novo preço: '))
                    self._estoque[codigo_barras].atualizar_preco(preco)
                    print('preço atualizado...')

    def vender_medicamento(self):
        codigo_barras = input('Codigo de barras medicamento: ')

        if codigo_barras in self._estoque:

            if self._estoque[codigo_barras].get_qtd > 0:

                print('Medicamento encontrado')
                print(self._estoque[codigo_barras].__str__())

                qtd = int(input('quandidades: '))

                if(qtd > self._estoque[codigo_barras].get_qtd > 0):
                    print('Estoque insificiente')
                else:
                    print('Venda realizada...')
                    self._estoque[codigo_barras].decrementar_qtd(qtd)

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
            print(f'Codigo barras: {medicamento.get_codigo_barras}')
            print(f'Nome: {medicamento.get_nome}')
            print(f'Preço: {medicamento.get_preco}')
            print(f'Quantidade estoque: {medicamento.get_qtd}')
            print('--------------')

    def db_carregar_medicamentos(self):
        db = Database()
        dados = db.get_medicamentos() #retorna uma lista de conjuntos

        for medicamento in dados:
            remedio = Remedio()
            remedio.set_remedio(medicamento[0], medicamento[1], medicamento[2], medicamento[3])
            self._estoque[medicamento[0]] = remedio