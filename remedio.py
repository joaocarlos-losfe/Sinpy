
from base_de_dados import Database

class Remedio():
    def __init__(self):
        self._nome = None
        self._codigo_barras = None
        self._qtd = None
        self._preco = None

    def set_remedio(self,codigo_barras, nome, qtd, preco):
        if self._codigo_barras is None:
            self._nome = nome
            self._codigo_barras = codigo_barras
            self._qtd = qtd
            self._preco = preco

            try:
                self.db_salvar(codigo_barras, nome , qtd, preco)
            except:
                pass

            print('cadastrado...')

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_codigo_barras(self):
        return self._codigo_barras

    @property
    def get_qtd(self):
        return self._qtd

    @property
    def get_preco(self):
        return  self._preco

    def __str__(self):
        print(f'Codigo barras: {self.get_codigo_barras}')
        print(f'Nome: {self.get_nome}')
        print(f'Preço: {self.get_preco}')
        print(f'Quantidade estoque: {self.get_qtd}')
        print('--------------\n')

    def decrementar_qtd(self, qtd):
        self._qtd -= qtd

    def incrementar_qtd(self, qtd):
        self._qtd -= qtd

    def db_salvar(self, codigo_barras, nome, qtd, preco):
        db = Database()
        db.salvar(codigo_barras, nome, qtd, preco)

    def db_atualizar(self):
        pass

    def db_deletar(self):
        pass