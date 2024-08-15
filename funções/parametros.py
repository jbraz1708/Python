def somar(a=0,b=0,c=0): #parametros opcionais
    """Fazer a soma dos valores e mostrar o resultado na tela

    Args:
        a (int): primeiro valor
        b (int): segundo valor
        c (int): terceiro valor
    """
    s = a + b + c 
    print(f'A soma vale {s}')

help(somar)
somar()