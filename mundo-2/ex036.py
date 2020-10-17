# Exercício 036 - Aprovando Empréstimo

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário de comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / anos / 12
empréstimo = 'NEGADO!' if prestação > 0.30 * salário else 'APROVADO!'

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R${prestação:.2f}')
print(f'Empréstimo {empréstimo}')
