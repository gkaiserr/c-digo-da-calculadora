def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

while True:
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 5:
        print("Saindo da calculadora.")
        exit()

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(num1, num2)
        operacao = "+"
        operacaon = "soma"
    elif opcao == 2:
        resultado = subtracao(num1, num2)
        operacao = "-"
        operacaon = "subtração"
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
        operacao = "*"
        operacaon = "multiplicação"
    elif opcao == 4:
        resultado = divisao(num1, num2)
        operacao = "/"
        operacaon = "divisão"
    else:
        print("Opção inválida!")
        continue

    print(f"A operação foi {operacaon}: {num1} {operacao} {num2} = {resultado}")
