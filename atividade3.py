#abstração, encapsulamento e herança.

class Funcionario:
    def __init__(self, nome, cargo, salario=0):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario

    def obter_salario(self):
        return self._salario
    
    def aumento_salarial(self,aumento):
        if aumento > 0:
            self._salario += aumento
        else:
            print("Você não ganhou Aumento salarial!")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario=0):
        super().__init__(nome, cargo, salario)

    def ajuste_salario(self, novo_salario):
        self._salario = novo_salario
        
    def bonus(self, bonus):
        if bonus > 0:
            novo_salario = bonus + self.obter_salario()
            self.ajuste_salario(novo_salario)
        else:
            print("Valor Inválido!")


f1 = Funcionario("Edson", "Motorista", 1400)
f2 = Funcionario("Edvan", "cobrador", 1000)
g1 = Gerente("Edinilton", "Gerente", 2500)

print(f"O funcionário {f1.nome},{f1.cargo}, recebe o salario de {f1._salario}")
print(f"O funcionário {f2.nome},{f2.cargo}, recebe o salario de {f2._salario}")
print(f"O funcionário {g1.nome},{g1.cargo}, recebe o salario de {g1._salario}\n")


f1.aumento_salarial(300)
f2.aumento_salarial(300)
g1.bonus(1000)

print(f"O funcionário {f1.nome},{f1.cargo}, Após receber aumento, seu novo salário é:{f1._salario}")
print(f"O funcionário {f2.nome},{f2.cargo}, Após receber aumento, seu novo salário é:{f2._salario}")
print(f"O funcionário {g1.nome},{g1.cargo}, Após receber um bonus, seu novo salário é:{g1._salario}")



        

        
        
