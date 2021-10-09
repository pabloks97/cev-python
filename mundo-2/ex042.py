# Exercício 042 - Analisando Triângulos v2.0

from cev.utils import triangulo, equilatero, isosceles

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if not triangulo(a, b, c):
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
elif equilatero(a, b, c):
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif isosceles(a, b, c):
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
