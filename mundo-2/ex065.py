# Exercício 065 - Maior e Menor Valores

números = []
continuar = 's'

while continuar in 'sS':
    números.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N] ')

média = sum(números) / len(números)
maior = max(números)
menor = min(números)

print(f'Você digitou {len(números)} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
