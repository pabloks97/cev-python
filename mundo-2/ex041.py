# Python 041 - Classificando Atletas

from datetime import datetime
ano_atual = datetime.now().year

nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - nascimento

if idade <= 9:
    classificação = 'MIRIM'
elif idade <= 14:
    classificação = 'INFANTIL'
elif idade <= 19:
    classificação = 'JUNIOR'
elif idade <= 25:
    classificação = 'SÊNIOR'
else:
    classificação = 'MASTER'

print(f'O atleta tem {idade} anos.')
print(f'Classificação: {classificação}')
