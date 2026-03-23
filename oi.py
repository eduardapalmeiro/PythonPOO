import math

class Produto:
    def __init__(self, codigo, descricao, preco, custo):
        self.codigo = int(codigo)
        self.descricao = str(descricao)
        self.preco = float(preco)
        self.custo = float(custo)

    def setCodigo(self, codigo):
        self.codigo = codigo
        
    def setDescricao(self, descricao):
        self.descricao = descricao
        
    def setPreco(self, novo_preco):
        
        limiteadd = self.preco + (self.preco * 0.10)
        limitesub = self.preco - (self.preco * 0.10)
        
        # Verifica se o novo preço está fora da margem permitida
        if novo_preco > limiteadd or novo_preco < limitesub:
            print(f"\nO preço não pode ser alterado em mais de 10%.")
        else:
            self.preco = novo_preco
            print("\nPreço alterado com sucesso!")
            
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
        if self.preco == 0:
            return 0
        lucro = ((self.preco - self.custo) / self.preco) * 100
        return math.trunc(lucro)

p1 = Produto(1, "Motog", 1500.00, 900.00)
p2 = Produto(2, "IphoneX", 3000.00, 2300.00)
p3 = Produto(3, "Redminote", 2000.00, 1000.00)
p4 = Produto(4, "GalaxyZ", 3000.00, 2200.00)

lista_produtos = [p1, p2, p3, p4]

def buscar_produto_por_codigo(codigo):
    for p in lista_produtos:
        if p.getCodigo() == codigo:
            return p
    return None

while True:
    print("***********************************")
    print("SISTEMA DE GESTÃO DE PRODUTOS")
    print("***********************************")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Calcular a margem de lucro de um produto")
    print("4 - Alterar dados do produto")
    print("5 - Sair")
    print("***********************************")

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == '1':
        print("\nCadastrar novo produto")
        codigo = int(input("Digite o código: "))
        
        if buscar_produto_por_codigo(codigo) is not None:
            print("\nJá existe um produto cadastrado com este código.")
        else:
            descricao = input("Digite a descrição: ")
            preco = float(input("Digite o preço: "))
            custo = float(input("Digite o custo: "))
            
            novo_produto = Produto(codigo, descricao, preco, custo)
            lista_produtos.append(novo_produto)
            print("\nProduto cadastrado com sucesso!")

    elif opcao == '2':
        print("\nLista de produtos cadastrados:")
        for p in lista_produtos:
            print(f"Código: {p.getCodigo():<3} | Descrição: {p.getDescricao():<12} | Preço: R${p.getPreco():<8.2f} | Custo: R${p.getCusto():.2f}")

    elif opcao == '3':
        print("\nCalcular margem de lucro:")
        codigo = int(input("Informe o código do produto: "))
        produto = buscar_produto_por_codigo(codigo)
        
        if produto:
            print(f"\nProduto: {produto.getDescricao()}")
            print(f"Margem de lucro: {produto.calculaMargem()}%")
        else:
            print("\nProduto não encontrado.")

    elif opcao == '4':
        print("\nAlterar dados do produto")
        codigo = int(input("Informe o código do produto que deseja alterar: "))
        produto = buscar_produto_por_codigo(codigo)
        
        if produto:
            print(f"\nAlterando o produto: {produto.getDescricao()}")
            
            nova_descricao = input(f"Nova descrição (Atual: {produto.getDescricao()} - Pressione Enter para manter): ")
            if nova_descricao != "":
                produto.setDescricao(nova_descricao)
                
            novo_preco_str = input(f"Novo preço (Atual: R${produto.getPreco():.2f} - Pressione Enter para manter): ")
            if novo_preco_str != "":
                novo_preco = float(novo_preco_str)
                produto.setPreco(novo_preco)
                
            novo_custo_str = input(f"Novo custo (Atual: R${produto.getCusto():.2f} - Pressione Enter para manter): ")
            if novo_custo_str != "":
                produto.setCusto(float(novo_custo_str))
                print("Custo alterado.")
                
        else:
            print("\nProduto não encontrado.")

    elif opcao == '5':
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
