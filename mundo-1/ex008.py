# Exercício 008 - Conversor de Medidas

d = float(input('Uma distância em metros: '))

print(f'A medida de {d}m corresponde a')
print(f'{d / 1000}km\n{d / 100}hm\n{d / 10}dam')
print(f'{(d * 10):.0f}dm\n{(d * 100):.0f}cm\n{(d * 1000):.0f}mm')
