# Exercício 015 - Aluguel de Carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km

print(f'O total a pagar é de R${total:.2f}')
