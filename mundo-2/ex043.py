# Exercício 043 - Índice de Massa Corporal

from utils import imc

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

imc = imc(peso, altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
