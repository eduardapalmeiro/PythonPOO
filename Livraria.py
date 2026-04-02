class Livro:
    def __init__(self, codigoLivro, titulo, codigoISBN, editoraLivro):
        self.codigoLivro = int(codigoLivro)
        self.titulo = str(titulo)
        self.codigoISBN = str(codigoISBN)
        self.editoraLivro = editoraLivro

    def setCodigoLivro(self, codigoLivro):
        self.codigoLivro = codigoLivro
        
    def setTitulo(self, titulo):
        self.titulo = titulo
        
    def setCodigoISBN(self, codigoISBN):
        self.codigoISBN = codigoISBN
            
    def setEditoraLivro(self, editoraLivro):
        self.editoraLivro = editoraLivro

    def getCodigoLivro(self):
        return self.codigoLivro
        
    def getTitulo(self):
        return self.titulo
        
    def getCodigoISBN(self):
        return self.codigoISBN
        
    def getEditoraLivro(self):
        return self.editoraLivro
        
class Editora:
    def __init__(self, codigoEditora, razaoSocial, nomeContato, telefone):
        self.codigoEditora = int(codigoEditora)
        self.razaoSocial = str(razaoSocial)
        self.nomeContato = str(nomeContato)
        self.telefone = str(telefone)

    def setCodigoEditora(self, codigoEditora):
        self.codigoEditora = codigoEditora
        
    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial
        
    def setNomeContato(self, nomeContato):
        self.nomeContato = nomeContato
            
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCodigoEditora(self):
        return self.codigoEditora
        
    def getRazaoSocial(self):
        return self.razaoSocial
        
    def getNomeContato(self):
        return self.nomeContato
        
    def getTelefone(self):
        return self.telefone

e1 = Editora(1, 'Fogo', 'Renata', '51912345678')
e2 = Editora(2, 'Agua', 'Sylas', '51967676767')
e3 = Editora(3, 'Terra', 'Violet', '5195555555')

l1 = Livro(1, 'Almanaque do Cebolinha', '6767676767676', e1)
l2 = Livro(2, 'Crime e castigo', '1234567890123', e2)
l3 = Livro(3, 'Metamorfose', '3333333333333', e2)

lista_editoras = [e1, e2, e3]
lista_livros = [l1, l2, l3]

def buscar_editora_por_razao_social(razaoSocial):
    for e in lista_editoras:
        if e.getRazaoSocial() == razaoSocial:
            return e
    return None
    
def buscar_livro_por_titulo(titulo):
    for l in lista_livros:
        if l.getTitulo() == titulo:
            return l
    return None
    
def buscar_editora_por_codigo(codigoEditora):
    for e in lista_editoras:
        if e.getCodigoEditora() == codigoEditora:
            return e
    return None

def buscar_livro_por_codigo(codigoLivro):
    for l in lista_livros:
        if l.getCodigoLivro() == codigoLivro:
            return l
    return None
    
def listar_editoras_para_livros():
    for e in lista_editoras:
        print(e.getRazaoSocial())
        
def cadastrar_livro():
    print("\nCadastrar novo livro")
    codigoLivro = int(input("Digite o código: "))
        
    if buscar_livro_por_codigo(codigoLivro) is not None:
        print("\nJá existe um livro cadastrado com este código.")
    else:
        titulo = input("Digite o título: ")
        codigoISBN = input("Digite o codigo ISBN do livro: ")
        listar_editoras_para_livros()
        editora = input("Escolha uma editora existente: ")
            
        editoraLivro = None

        for e in lista_editoras:
            if editora == e.getRazaoSocial():
                editoraLivro = e
                break

        if editoraLivro is None:
            print("\nA editora não existe.")
            return
            
        novo_livro = Livro(codigoLivro, titulo, codigoISBN, editoraLivro)
        lista_livros.append(novo_livro)
        print("\nLivro cadastrado com sucesso!")

while True:
    print("***********************************")
    print("SISTEMA DE GESTÃO DE LIVRARIA")
    print("***********************************")
    print("1 - Cadastrar editora")
    print("2 - Cadastrar livro")
    print("3 - Pesquisar editora")
    print("4 - Pesquisar livro")
    print("5 - Sair")
    print("***********************************")

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == '1':
        print("\nCadastrar nova editora")
        codigoEditora = int(input("Digite o código: "))
        
        if buscar_editora_por_codigo(codigoEditora) is not None:
            print("\nJá existe uma editora cadastrada com este código.")
        else:
            razaoSocial = input("Digite a razão social: ")
            nomeContato = input("Digite o nome de contato: ")
            telefone = input("Digite o telefone: ")
            
            nova_editora = Editora(codigoEditora, razaoSocial, nomeContato, telefone)
            lista_editoras.append(nova_editora)
            print("\nEditora cadastrada com sucesso!")

    elif opcao == '2':
        cadastrar_livro()
            
    elif opcao == '3':
        print("\nPesquisar editora:")
        razaoSocial = input("Informe a razão social da editora: ")
        editora = buscar_editora_por_razao_social(razaoSocial)
        
        if editora:
            print(f"\nInformações da editora: {editora.getCodigoEditora()} | {editora.getRazaoSocial()} | {editora.getNomeContato()} | {editora.getTelefone()}")
        else:
            print("\nEditora não encontrada.")

    elif opcao == '4':
        print("\nPesquisar livro:")
        titulo = input("Informe o titulo do livro: ")
        livro = buscar_livro_por_titulo(titulo)
        
        if livro:
            print(f"\nInformações do livro: {livro.getCodigoLivro()} | {livro.getTitulo()} | {livro.getCodigoISBN()} | {livro.editoraLivro.getRazaoSocial()}")
        else:
            print("\nLivro não encontrado.")

    elif opcao == '5':
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
