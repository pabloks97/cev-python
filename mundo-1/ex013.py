# Exercício 013 - Reajuste Salarial

from utils import porcento

salário = float(input('Qual é o salário do Funcionário? R$'))
aumento = porcento(15, salário)
total = salário + aumento

print(f'Um funcionário que ganhava R${salário:.2f}, ', end='')
print(f'com 15% de aumento, passa a receber R${total:.2f}')
