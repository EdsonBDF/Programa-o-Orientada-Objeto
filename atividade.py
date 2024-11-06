#Faça uma classe de pessoas com os seguintes atributos:Nome, Idade, Peso e altura
#Crie um método para imprimir todos os dados de uma pessoa
#Crie um método para calcular quantos anos a pessoa terá daqui a x anos, sendo x um parêmetro
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome  
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f"\nnome:{self.nome} \nIdade:{self.idade} \nPeso:{self.peso} \nAltura:{self.altura}"    
    
    def update_idade(self, x):
        new_idade = self.idade +x 
        print(f"Daqui a {x} anos,a idade de {self.nome} será {new_idade}")

p1 = Pessoa("Maria", 32, 58, 1.66)
print(p1)
p1.update_idade(10)