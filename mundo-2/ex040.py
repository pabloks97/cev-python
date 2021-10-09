# Exercício 040 - Aquele Clássico da Média

from cev.utils import media

notas = []
notas.append(float(input('Primeira nota: ')))
notas.append(float(input('Segunda nota: ')))

valor_media = media(notas)

print(f'Tirando {notas[0]} e {notas[1]} a média do aluno é {valor_media:.1f}')

if valor_media < 5:
    resultado = 'REPROVADO'
elif valor_media >= 7:
    resultado = 'APROVADO'
else:
    resultado = 'de RECUPERAÇÃO'
print(f'O aluno está {resultado}.')
