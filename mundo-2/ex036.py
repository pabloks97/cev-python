# Exercício 036 - Aprovando Empréstimo

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário de comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / anos / 12
emprestimo = 'NEGADO!' if prestacao > 0.30 * salario else 'APROVADO!'

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R${prestacao:.2f}')
print(f'Empréstimo {emprestimo}')
