# Exercício 048 - Soma Ímpares Múltiplos de Três

soma = valores = 0
for impar in range(1, 500, 2):
    if impar % 3 == 0:
        soma += impar
        valores += 1
print(f'A soma de todos os {valores} valores solicitados é {soma}')
