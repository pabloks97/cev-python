# Exercício 008 - Conversor de Medidas

distancia = float(input('Uma distância em metros: '))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10

dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print(f'A medida de {distancia}m corresponde a')
print(f'{km}km\n{hm}hm\n{dam}dam')
print(f'{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
