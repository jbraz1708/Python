def soma (n1,n2):
    return n1 + n2
def subtração (n1,n2):
    return n1 - n2
def divisão (n1,n2):
    return n1 / n2 
def multiplicação (n1,n2):
    return n1 * n2

n1 = float(input('digite um número: '))
n2 = float(input('digite um número: '))
print("""  ======= Selecione uma operação ======= 
[1] divisão
[2] multiplicação
[3] soma
[4] subtração""")
option = int(input('Escolha uma opção: '))
if option == 1:
    if n1 == 0 and n2 == 0:
        print('não foi possível realizar a divisão')
    else:
        print(f"A divisão entre {n1} e {n2} é: {divisão(n1,n2)}")
elif option == 2:
    print(f"A multiplicação entre {n1} e {n2} é: {multiplicação(n1,n2)}")
elif option == 3:
    print(f"A soma entre {n1} e {n2} é: {soma(n1,n2)}")
elif option == 4:
    print(f"A subtração entre {n1} e {n2} é: {subtração(n1,n2)}")
else:
    print("Escolha uma opção correta!")