# Correto! A classe Retangulo está correta e define os atributos __x, __y e __area, além do construtor e o método obter_area(). Nada impede então criar um objeto:
# r = Retangulo(7,6)COPIAR CÓDIGO
# Agora, se você tenta acessar um atributo area, que na verdade não declaramos, o Python cria automaticamente um novo atributo e inicializa com o valor 7:
# r.area = 7COPIAR CÓDIGO
# Na linha em cima o objeto ganha um novo atributo com o nome area. Ou seja, temos um atributo __area E um novo com o nome area. No entanto, ao chamar r.obter_area(), continuamos acessar o atributo __area que foi inicializado com o produto de 7*6!

class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area

