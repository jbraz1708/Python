"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média atingida pelo aluno foi de: {media}')
if media < 5:
    print('reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!!')