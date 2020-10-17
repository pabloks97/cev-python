# Exercício 048 - Soma Ímpares Múltiplos de Três

soma = valores = 0
for ímpar in range(1, 500, 2):
    if ímpar % 3 == 0:
        soma += ímpar
        valores += 1
print(f'A soma de todos os {valores} valores solicitados é {soma}')
