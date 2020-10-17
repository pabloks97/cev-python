# Exercício 037 - Conversor de Bases Numéricas

número = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{número} convertido para BINÁRIO é igual a {número:b}')
elif opção == 2:
    print(f'{número} convertido para OCTAL é igual a {número:o}')
elif opção == 3:
    print(f'{número} convertido para HEXADECIMAL é igual a {número:x}')
