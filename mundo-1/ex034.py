# Exercício 034 - Aumentos Múltiplos

from utils import porcento

salario = float(input('Qual é o salário do funcionário? R$'))

porcentagem = 10 if salario > 1250 else 15
aumento = porcento(porcentagem, salario)

total = salario + aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${total:.2f} agora.')
