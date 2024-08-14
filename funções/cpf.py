def calcula_digitos_parcial(cpf_parcial):
    soma = 0
    for i in range(9):
        soma += int(cpf_parcial[i]) * (10 - i)
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0

    cpf_parcial.append(str(primeiro_digito))

    soma = 0
    for i in range(10):
        soma += int(cpf_parcial[i]) * (11 - i)
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0

    return primeiro_digito, segundo_digito

# Combinations to test
combinations = ["084", "165", "246", "327", "408", "599", "750", "831", "912"]

# Test each combination
for comb in combinations:
    cpf_completo = [int(d) for d in comb + "20014465"]
    primeiro_digito, segundo_digito = calcula_digitos_parcial(cpf_completo[:9])
    if [primeiro_digito, segundo_digito] == [1, 9]:
        print(f"O CPF válido é: {comb}.200.144-65")