class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instance = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instance
        return cls._instancias[cls]

class Singleton(metaclass=SingletonMeta):

    def metodo_qualquer(self):
        pass

if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if s1 is s2:
        print('instancias SÃO iguais...')
    else:
        print('Instancias NÃO são iguais')