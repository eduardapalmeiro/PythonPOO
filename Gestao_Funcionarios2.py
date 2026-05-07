class Empregado():
    def __init__(self, nome):
        self.nome = str(nome)

    def retornaPagamento(self):
        return 0.0

class Assalariado(Empregado):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def retornaPagamento(self):
        return self.salario

class Horista(Empregado):
    def __init__(self, nome, valorHora, quandidadeDeHoras):
        super().__init__(nome)
        self.valorHora = valorHora
        self.quandidadeDeHoras = quandidadeDeHoras

    def retornaPagamento(self):
        return self.valorHora * self.quandidadeDeHoras * 4.5

fun1 = Assalariado('Sara', 2000.00)
fun2 = Horista('Jonas', 40.00,44.00)

folhaPagamento = [fun1,fun2]

def cadastrarAssalariado():
    print('\nCadastrar novo assalariado: ')

    novoNome = input('\nDigite o nome do assalariado: ')
    novoSalario = float(input('\nDigite o salário do assalariado: '))

    novo_assalariado = Assalariado(novoNome, novoSalario)
    folhaPagamento.append(novo_assalariado)
    print("\nVendedor assalariado com sucesso!")

def cadastrarHorista():
    print('\nCadastrar novo horista: ')

    novoNome = input('\nDigite o nome do horista: ')
    novoVH = input('\nDigite o valor da hora: ')
    novaQH = input('\nDigite a quantidade de horas:')


    novo_horista = Horista(novoNome, novoVH, novaQH)
    folhaPagamento.append(novo_horista)
    print("\nVendedor assalariado com sucesso!")

while True:
    print("***********************************")
    print("SISTEMA DE CADASTRO DE FUNCIONÁRIOS")
    print("***********************************")
    print("1 - Cadastrar Assalariado")
    print("2 - Cadastrar Horista")
    print("3 - Calcular folha e sair")
    print("***********************************")

    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == '1':
        cadastrarAssalariado()

    elif opcao == '2':
        cadastrarHorista()

    elif opcao == '3':
        total = 0
        print("Folha de pagamento: ")

        for empregado in folhaPagamento:
            pagamento = empregado.retornaPagamento()
            total += pagamento
            print(f"Nome: {empregado.nome} | Pagamento: R$ {pagamento:.2f}")

        print(f"Total gasto pela empresa: {total:.2f}")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
