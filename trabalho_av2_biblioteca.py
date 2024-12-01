from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    @abstractmethod
    def exibir_dados(self):
        pass

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3:
            if livro.disponivel:
                self.livros_emprestados.append(livro)
                livro.disponivel = False
            else:
                print(f"O livro '{livro.titulo}' não está disponível para empréstimo.")
        else:
            print("O usuário já possui 3 livros emprestados.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True

    def exibir_dados(self):
        return f"Usuário: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Livros Emprestados: {len(self.livros_emprestados)}"

class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)

    def cadastrar_livro(self, livro, biblioteca):
        biblioteca.adicionar_livro(livro)

    def cadastrar_usuario(self, usuario, biblioteca):
        biblioteca.adicionar_usuario(usuario)

    def exibir_dados(self):
        return f"Administrador: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def exibir_dados(self):
        pass

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor)
        self.ano = ano

    def exibir_dados(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponível: {self.disponivel}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        return [livro for livro in self.livros if livro.disponivel]

    def listar_usuarios_com_livros(self):
        return [usuario for usuario in self.usuarios if usuario.livros_emprestados]

def menu():
    biblioteca = Biblioteca()
    
    admin = Administrador("Edson", 25, "0001")

    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Adicionar Usuário")
        print("3. Empréstimo de Livro")
        print("4. Devolução de Livro")
        print("5. Listar Livros Disponíveis")
        print("6. Listar Usuários com Livros Emprestados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano = input("Ano de Publicação: ")
            livro = Livro(titulo, autor, ano)
            admin.cadastrar_livro(livro, biblioteca)
            print(f"Livro '{titulo}' cadastrado com sucesso.")

        elif opcao == "2":
            nome = input("Nome do Usuário: ")
            idade = int(input("Idade do Usuário: "))
            matricula = input("Matrícula do Usuário: ")
            usuario = UsuarioComum(nome, idade, matricula)
            admin.cadastrar_usuario(usuario, biblioteca)
            print(f"Usuário '{nome}' cadastrado com sucesso.")

        elif opcao == "3":
            matricula = input("Matrícula do Usuário: ")
            titulo = input("Título do Livro: ")

            usuario = next((u for u in biblioteca.usuarios if u.matricula == matricula), None)
            livro = next((l for l in biblioteca.livros if l.titulo == titulo), None)

            if usuario and livro:
                usuario.emprestar_livro(livro)
                print(f"Livro '{titulo}' emprestado para {usuario.nome}.")
            else:
                print("Usuário ou Livro não encontrado.")

        elif opcao == "4":
            matricula = input("Matrícula do Usuário: ")
            titulo = input("Título do Livro: ")

            usuario = next((u for u in biblioteca.usuarios if u.matricula == matricula), None)
            livro = next((l for l in biblioteca.livros if l.titulo == titulo), None)

            if usuario and livro:
                usuario.devolver_livro(livro)
                print(f"Livro '{titulo}' devolvido por {usuario.nome}.")
            else:
                print("Usuário ou Livro não encontrado.")

        elif opcao == "5":
            print("\nLivros Disponíveis:")
            for livro in biblioteca.listar_livros_disponiveis():
                print(livro.exibir_dados())

        elif opcao == "6":
            print("\nUsuários com Livros Emprestados:")
            for usuario in biblioteca.listar_usuarios_com_livros():
                print(usuario.exibir_dados())

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
