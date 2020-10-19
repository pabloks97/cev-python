# Exercício 079 - Valores Únicos em uma Lista

valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    if input('Quer continuar? [S/N] ') in 'nN': break

print(f'Você digitou os valores {sorted(valores)}')
