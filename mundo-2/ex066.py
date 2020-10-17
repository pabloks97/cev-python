# Exercício 066 - Vários Números com Flag

soma = valores = 0
while True:
    número = int(input('Digite um valor (999 para parar): '))
    if número == 999:
        break
    soma += número
    valores += 1
print(f'A soma dos {valores} valores foi {soma}!')
