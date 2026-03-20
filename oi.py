import math

class Produtos:
    def __init__(self, codigo, descricao, preco, custo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.custo = custo

    def setCodigo(self, codigo):
        self.codigo = codigo
    def setDescricao(self, descricao):
        self.descricao = descricao
    def setPreco(self, preco):
        if self.preco < self.preco + (self.preco * 0.1) or self.preco > self.preco - (self.preco * 0.1):
            print(f"O preço não pode ser alterado em mais de 10% do valor original.")
        else:
            self.preco = preco
    def setCusto(self, custo):
        self.custo = custo

    def getCodigo(self):
        return self.codigo
    def getDescricao(self):
        return self.descricao
    def getPreco(self):
        return self.preco
    def getCusto(self):
        return self.custo

    def calculaMargem(self):
        self.lucro = ((self.preco - self.custo) / self.preco) * 100
        print(f"{math.trunc(self.lucro)}%")

p1 = Produtos(1, "Motog",1500.00,900.00)
p2 = Produtos(2, "IphoneX",3000.00,2300.00)
p3 = Produtos(3, "Redminote",2000.00,1000.00)
p4 = Produtos(4, "GalaxyZ",3000.00,2200.00)

while True:
    print("\nCadastrar novo produto:")
    codigo = int(input("Digite o codigo do produto: "))
    
