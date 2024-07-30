# Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
# No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor,
#  um de cada. Depois precisa executar a operação e mostrar o resultado na tela.
# Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.


def calculadora(a, b, op):

    if (op == 1):
        res = a+b

    elif (op == 2):
        res = a-b

    elif (op == 3):
        res = a*b

    elif (op == 4):
        res = a/b

    return res


while True:
    op = int(input(
        "Qual a operacao desejada? \n 1. Soma \n 2. Subtração\n 3. Multiplicação\n 4. Divisão \n 0: Sair\n"))
    if (op == 0):
        break
    elif (op < 1) or (op > 4):
        print("Essa opção não existe \n\n")
    else:
        a = int(input("Qual o primeiro numero ?\n"))
        b = int(input("Qual o segundo numero?\n"))
        c = calculadora(a, b, op)
        print("resposta = \n", c)
