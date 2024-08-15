
def contador (i,f,p):
    #docString(manual a ser exibido da ajuda interativa)
    """Faz uma contagem e mostra na tela

    Args:
        i (_type_): início da contagem
        f (_type_): fim da contagem   
        p (_type_): passo da contagem
    """
    c = i
    while i <= f:
        print(f'{c}', end='')
        c+=p
    print('Fim!!')

help(contador)
 