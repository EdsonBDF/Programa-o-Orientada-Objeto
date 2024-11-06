class Contabancaria:
    def __init__(self, titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"\nTITULAR DA CONTA:{self.titular}\nSALDO ATUAL:R$ {self.saldo}" 
    
    def depositar(self, valor):
        if valor > 0:
           self.saldo = self.saldo + valor
           print(f"Deposito de R$ {valor:.2f} realizado com sucesso! Seu novo saldo é: R$ {self.saldo}")
        else:
           print("Valor inválido!")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo: 
           self.saldo = self.saldo - valor
           print(f"Saque de R$ {valor:.2f} realizado com sucesso! Seu novo saldo é: R$ {self.saldo}")
        else:
           print(f"Valor inválido! Saque de R$ {valor:.2f} Não autorizado!")

p1 = Contabancaria("Edson Silva",1000)
print(p1)

p1.depositar(1000)
print(p1)

p1.saque(3000)
print(p1)