class Livro:
    def __init__(self,titulo):
        self.titulo = titulo
        self.foi_lido = False

    def marcar_como_lido(self):
        self.foi_lido = True
        print(f'O livro "{self.titulo}" foi lido.')

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def ler_livro(self, livro):
        print(f'{self.nome} Está lendo o livro "{livro.titulo}".')
        livro.marcar_como_lido()

livro1 = Livro("O senhor dos Anéis")
pessoa = Pessoa("Edson")

pessoa.ler_livro(livro1)        