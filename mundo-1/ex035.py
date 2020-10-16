# Exercício 035 - Analisando Triângulo v1.0

from utils import é_triângulo

print(10 * '-=-')
print('Analisador de Triângulos')
print(10 * '-=-')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

resultado = 'PODEM FORMAR' if é_triângulo(a, b, c) else 'NÃO PODEM FORMAR'
print(f'Os segmentos acima {resultado} triângulo!')
