from remedio import Remedio
from base_de_dados import Database
import sys
class Farmacia:
    def __init__(self):
        self._estoque = {}

    def abrir_farmacia(self):

        self.db_carregar_medicamentos()

        while True:
            print('0 - Sair')
            print('1 - cadastrar medicamento')
            print('2 - ver estoque')
            print('3 - atualizar medicamento')
            print('> ')
            op = input()
            if op == '0':
                exit()
            elif op == '1':
                self.cadastrar_medicamento()
            elif op == '2':
                self.mostrar_estoque()
            elif op == '3':
                self.atualizar_medicamento()
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
            print(f'Codigo barras: {medicamento.get_codigo_barras}')
            print(f'Nome: {medicamento.get_nome}')
            print(f'Preço: {medicamento.get_preco}')
            print(f'Quantidade estoque: {medicamento.get_qtd}')
            print('--------------')

    def atualizar_medicamento(self):
        codigo_barras = input('codigo de barras: ')

        if codigo_barras in self._estoque:
            if self._estoque[codigo_barras].get_qtd == 0:
                print('atenção, medicamento precisa ser reposto..')

            print('1 - atualizar nome')
            print('2 - atualizar preço')
            print('3 - incrementar estoque')

            op = input()

            if op == '1':
                nome = input('Novo nome: ')
                self._estoque[codigo_barras].atualizar_nome(nome)
                print('Nome atualizado...\n')

            elif op == '2':
                preco = float(input('Novo preço: '))
                self._estoque[codigo_barras].atualizar_preco(preco)
                print('Preco atualizado\n')

            elif op == '3':
                qtd = int(input('Quantidade: '))
                self._estoque[codigo_barras].atualizar_qtd(qtd)
                print('Quantidade atualizada\n')

    def db_carregar_medicamentos(self):
        db = Database()
        dados = db.get_medicamentos() #retorna uma lista de conjuntos

        for medicamento in dados:
            remedio = Remedio()
            remedio.set_remedio(medicamento[0], medicamento[1], medicamento[2], medicamento[3])
            self._estoque[medicamento[0]] = remedio
