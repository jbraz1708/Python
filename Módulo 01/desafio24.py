""" Faça um programa que leia o nome da cidade e diga se começa com santo ou não """
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')