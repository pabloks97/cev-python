# Exercício 064 - Tratando Vários Valores v1.0

contador = soma = 0
número = int(input('Digite um número [999 para parar]: '))
while número != 999:
    soma += número
    contador += 1
    número = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
