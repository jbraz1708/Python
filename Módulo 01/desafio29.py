""""Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""

vel = int(input("Digite a velocidade do veículo ao passar no radar: "))
if vel > 80:
    print("Você foi multado!!")
    multa = vel - 80 
    valormulta = multa * 7.0
    print(f"A Multa aplicada foi de R$ {valormulta} ")
else:
    print("Velocidade permitida!")