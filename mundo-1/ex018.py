# Exercício 018 - Seno, Cosseno e Tangente

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))

radiano = radians(ângulo)

print(f'O ângulo de {ângulo} tem o SENO de {sin(radiano):.2f}')
print(f'O ângulo de {ângulo} tem o COSSENO de {cos(radiano):.2f}')
print(f'O ângulo de {ângulo} tem a TANGENTE de {tan(radiano):.2f}')
