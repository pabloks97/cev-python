# Exercício 015 - Aluguel de Carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preço_dias = dias * 60
preço_km = km * 0.15
total = preço_dias + preço_km

print(f'O total a pagar é de R${total:.2f}')
