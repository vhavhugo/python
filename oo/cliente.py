class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # se trata de uma propriedade, não precisa mais usar o ()
    # exemplo: cliente.nome - o atributa precisa ser privado
    # o metodo precisa ter o mesmo nome
    # Terminal - Cmder
    # from cliente import Cliente
    # cliente = Cliente("Hugo")
    # cliente.nome

    @property 
    def nome(self):
        # .title() deixa a primeira maiuscula
        print("chamando property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando setter name()')
        self.__nome = nome
        