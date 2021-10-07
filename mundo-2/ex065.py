# Exercício 065 - Maior e Menor Valores

numeros = []
continuar = 's'

while continuar in 'sS':
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N] ')

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f'Você digitou {len(numeros)} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
