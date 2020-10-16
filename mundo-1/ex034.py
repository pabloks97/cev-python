# Exercício 034 - Aumentos Múltiplos

from utils import porcento

salário = float(input('Qual é o salário do funcionário? R$'))

porcentagem = 10 if salário > 1250 else 15
aumento = porcento(porcentagem, salário)

total = salário + aumento
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${total:.2f} agora.')
