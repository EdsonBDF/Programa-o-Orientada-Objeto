from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f"\nMarca:{self.marca} \nModelo:{self.modelo} \nAno de Fabricação:{self.ano}"
     
    
    @abstractmethod
    def tipo_combustivel(self):
        pass

class carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas) -> None:
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def tipo_combustivel(self):
        return "Álcool/Gasolina"
    
class moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilidradas) -> None:
        super().__init__(marca, modelo, ano)
        self.cilidradas = cilidradas

    def tipo_combustivel(self):
        return "Gasolina"
    
class camião(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima) -> None:
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def tipo_combustivel(self):
        return "Diesel"
    
    
Carro = carro("Chevrolet","Prisma", 2012, 4)
Moto = moto("Honda","Titan", 2010, "150cc")
Camião = camião("Volvo","Continental", 2023, "50.00kg")

print(Carro)
print(f"Tipo de Combustível é: {Carro.tipo_combustivel()} ")
print(Moto)
print(f"Tipo de Combustível é: {Moto.tipo_combustivel()} ")
print(Camião)
print(f"Tipo de Combustível é: {Camião.tipo_combustivel()} ")
