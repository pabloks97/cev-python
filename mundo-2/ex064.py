# Exercício 064 - Tratando Vários Valores v1.0

contador = soma = 0
x = int(input('Digite um número [999 para parar]: '))
while x != 999:
    soma += x
    contador += 1
    x = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
