# Exercício 040 - Aquele Clássico da Média

from utils import média

notas = []
notas.append(float(input('Primeira nota: ')))
notas.append(float(input('Segunda nota: ')))

média = média(notas)

print(f'Tirando {notas[0]} e {notas[1]} a média do aluno é {média:.1f}')

if média < 5:
    resultado = 'REPROVADO'
elif média >= 7:
    resultado = 'APROVADO'
else:
    resultado = 'de RECUPERAÇÃO'
print(f'O aluno está {resultado}.')
