def dobra(lst):
    pos = 0
    while pos < len(lst):  
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 4, 6]
print(valores)
dobra(valores)
print(valores)