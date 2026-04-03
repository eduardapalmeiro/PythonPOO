class Montadora:
    def __init__(self, codigoMontadora, estado, razaoSocial):
        self.codigoMontadora = int(codigoMontadora)
        self.estado = str(estado)
        self.razaoSocial = str(razaoSocial)

    def setCodigoMontadora(self, codigoMontadora):
        self.codigoMontadora = codigoMontadora

    def setEstado(self, estado):
        self.estado = estado

    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial

    def getCodigoMontadora(self):
        return self.codigoMontadora

    def getEstado(self):
        return self.estado

    def getRazaoSocial(self):
        return self.razaoSocial


class Modelo:
    def __init__(self, codigoModelo, nome, montadoraModelo):
        self.codigoModelo = int(codigoModelo)
        self.nome = str(nome)
        self.montadoraModelo = montadoraModelo

    def setCodigoModelo(self, codigoModelo):
        self.codigoModelo = codigoModelo

    def setNome(self, nome):
        self.nome = nome

    def setMontadoraModelo(self, montadoraModelo):
        self.montadoraModelo = montadoraModelo

    def getCodigoModelo(self):
        return self.codigoModelo

    def getNome(self):
        return self.nome

    def getMontadoraModelo(self):
        return self.montadoraModelo

class Carro:
    def __init__(self, placa, modeloCarro, anoFabricacao):
        self.placa = str(placa)
        self.modeloCarro = modeloCarro
        self.anoFabricacao = int(anoFabricacao)

    def setPlaca(self, placa):
        self.placa = placa

    def setModeloCarro(self, modeloCarro):
        self.modeloCarro = modeloCarro

    def setAnoFabricacao(self, anoFabricacao):
        self.anoFabricacao = anoFabricacao

    def getPlaca(self):
        return self.placa

    def getModeloCarro(self):
        return self.modeloCarro

    def getAnoFabricacao(self):
        return self.anoFabricacao

mtd1 = Montadora(1, 'RS', 'Ford')
mtd2 = Montadora(2, 'PR', 'BYD')
mtd3 = Montadora(3, 'BA', 'Mercedes')

mdl1 = Modelo(1, 'Ranger', mtd1)
mdl2 = Modelo(2, 'Shark', mtd2)
mdl3 = Modelo(3, 'SUV', mtd3)

car1 = Carro('ABC0123', mdl1, 2016)
car2 = Carro('OII0111', mdl2, 2017)
car3 = Carro('TCH4000', mdl3, 2018)

lista_montadoras = [mtd1, mtd2, mtd3]
lista_modelos = [mdl1, mdl2, mdl3]
lista_carros = [car1, car2, car3]


def buscar_montadora_por_codigo(codigoMontadora):
    for a in lista_montadoras:
        if a.getCodigoMontadora() == codigoMontadora:
            return a
    return None


def buscar_modelo_por_codigo(codigoModelo):
    for o in lista_modelos:
        if o.getCodigoModelo() == codigoModelo:
            return o
    return None

def buscar_carro_por_placa(placa):
    for p in lista_carros:
        if p.getPlaca() == placa:
            return p
    return None

def listar_montadoras_para_modelos():
    for a in lista_montadoras:
        print(a.getRazaoSocial())


def cadastrar_modelo():
    print("\nCadastrar novo modelo")
    codigoModelo = int(input("Digite o código: "))

    if buscar_modelo_por_codigo(codigoModelo) is not None:
        print("\nJá existe um modelo cadastrado com este código.")
    else:
        nome = input("Digite o nome: ")
        listar_montadoras_para_modelos()
        montadora = input("Escolha uma montadora existente: ")

        montadoraModelo = None

        for a in lista_montadoras:
            if montadora == a.getRazaoSocial():
                montadoraModelo = a
                break

        if montadoraModelo is None:
            print("\nA montadora não existe.")
            return

        novo_modelo = Modelo(codigoModelo, nome, montadoraModelo)
        lista_modelos.append(novo_modelo)
        print("\nModelo cadastrado com sucesso!")

def listar_modelos_para_carros():
    for o in lista_modelos:
        print(o.getNome())

def cadastrar_carro():
    print("\nCadastrar novo carro")
    placa = input("Digite a placa: ")

    if buscar_carro_por_placa(placa) is not None:
        print("\nJá existe um carro cadastrado com esta placa.")
    else:
        listar_modelos_para_carros()
        modelo = input("Escolha um modelo existente: ")

        modeloCarro = None

        for o in lista_modelos:
            if modelo == o.getNome():
                modeloCarro = o
                break

        if modeloCarro is None:
            print("\nO modelo não existe.")
            return

        anoFabricacao = int(input("Digite o ano de fabricação: "))

        novo_carro = Carro(placa, modeloCarro, anoFabricacao)
        lista_carros.append(novo_carro)
        print("\nCarro cadastrado com sucesso!")


while True:
    print("***********************************")
    print("SISTEMA DE GESTÃO DE CARROS")
    print("***********************************")
    print("1 - Cadastrar montadora")
    print("2 - Cadastrar modelo")
    print("3 - Cadastrar carro")
    print("4 - Listar montadoras")
    print("5 - Listar modelos")
    print("6 - Listar carros")
    print("7 - Sair")
    print("***********************************")

    opcao = input("Escolha uma opção (1 a 7): ")

    if opcao == '1':
        print("\nCadastrar nova montadora")
        codigoMontadora = int(input("Digite o código: "))

        if buscar_montadora_por_codigo(codigoMontadora) is not None:
            print("\nJá existe uma montadora cadastrada com este código.")
        else:
            estado = input("Digite a sigla do estado: ")
            razaoSocial = input("Digite a razão social: ")

            nova_montadora = Montadora(codigoMontadora, estado, razaoSocial)
            lista_montadoras.append(nova_montadora)
            print("\nMontadora cadastrada com sucesso!")

    elif opcao == '2':
        cadastrar_modelo()

    elif opcao == '3':
        cadastrar_carro()

    elif opcao == '4':
        print("\nLista de montadoras cadastradas:")
        for a in lista_montadoras:
            print(
                f"Código: {a.getCodigoMontadora():<3} | Estado: {a.getEstado():<2} | Razão Social: {a.getRazaoSocial()}")

    elif opcao == '5':
        print("\nLista de modelos cadastrados:")
        for o in lista_modelos:
            print(
                f"Código: {o.getCodigoModelo():<3} | Nome: {o.getNome()} | Montadora: {o.getMontadoraModelo()}")

    elif opcao == '6':
        print("\nLista de carros cadastrados:")
        for p in lista_carros:
            print(
                f"Placa: {p.getPlaca():<7} | Modelo: {p.getModeloCarro()} | Ano de fabricação: {p.getAnoFabricacao():<4}")

    elif opcao == '7':
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
