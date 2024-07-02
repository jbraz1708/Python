"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado!"""
#Definindo as variáveis
salario = float(input('Digite seu salário: '))
vCasa = float(input('Qual o valor da casa que você deseja comprar? R$:  '))
qntAnos = int(input('Em quantos anos você deseja pagar essa casa? '))

#Variável da porcentagem 
minimo = salario * 30 / 100

#Calculando o valor das parcelas mensais
prestMensal = vCasa / (qntAnos * 12)

#Condição do Empréstimo
if prestMensal <= minimo:
     print(f'Emprestimo Aprovado, as parcelas vão ficar de R$ {prestMensal:.2f}')
else:
    print('Emprestimo Negado!')