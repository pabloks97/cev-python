# Exercício 043 - Índice de Massa Corporal

from utils import imc

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

valor_imc = imc(peso, altura)
print(f'O IMC dessa pessoa é de {valor_imc:.1f}')

if valor_imc < 18.5:
    print('Abaixo do peso')
elif valor_imc < 25:
    print('Peso ideal')
elif valor_imc < 30:
    print('Sobrepeso')
elif valor_imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
