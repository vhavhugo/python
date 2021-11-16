# from collections.abc import Sized

# class MinhaListagem(Sized):
#     def __init__(self, descricao):
#         self.descricao = descricao

#     def __str__(self):
#         return self.descricao

# lista = MinhaListagem('teste')
# print(lista)

from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)