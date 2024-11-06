#create class product
class Product:
    def __init__(self, name, price, qtd):
        self.name = name
        self.price = price
        self.qtd = qtd

    def __str__(self):
        return f"{self.name} - {self.price:.2f} - {self.qtd}"

    # Method Update_price
    def update_price(self, new_price):
        self.price = new_price
        print(f"O preço do Produto {self.name} foi atualizado para {self.price:.2f}")

    # Method Update_qtd
    def update_qtd(self, new_qtd):
        self.qtd = self.qtd-new_qtd
        print(f"A quantidade do Produto {self.name} foi atualizado para {self.qtd}")

    #create instance of product
p1 = Product("laptop", 1000, 5)
print(p1)

p1.update_price(1300)
print(p1)

p1.update_qtd(1)
print(p1)

