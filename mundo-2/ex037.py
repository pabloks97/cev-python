# Exercício 037 - Conversor de Bases Numéricas

numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {numero:b}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {numero:o}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {numero:x}')
