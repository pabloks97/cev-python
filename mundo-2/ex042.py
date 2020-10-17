# Exercício 042 - Analisando Triângulos v2.0

from utils import é_triângulo, é_equilátero, é_isósceles

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if not é_triângulo(a, b, c):
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
elif é_equilátero(a, b, c):
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif é_isósceles(a, b, c):
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
