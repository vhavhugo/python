class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
        
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    
def pega_todos_os_filmes():
    
meus_filmes = pega_todos_os_filmes()

for filme in meus_filmes:
    print(filme)