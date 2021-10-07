# Exercício 066 - Vários Números com Flag

soma = valores = 0
while True:
    x = int(input('Digite um valor (999 para parar): '))
    if x == 999:
        break
    soma += x
    valores += 1
print(f'A soma dos {valores} valores foi {soma}!')
