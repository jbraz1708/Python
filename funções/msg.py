"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""

def escreva(txt):
    print('=' *30)
    print(txt)
    print('=' *30)

msg = str(input('Digite uma frase para ser formatada: '))
escreva(msg)