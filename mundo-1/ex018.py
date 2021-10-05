# Exercício 018 - Seno, Cosseno e Tangente

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))

radiano = radians(angulo)

print(f'O ângulo de {angulo} tem o SENO de {sin(radiano):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radiano):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(radiano):.2f}')
