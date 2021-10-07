# Python 041 - Classificando Atletas

from datetime import datetime

ano_atual = datetime.now().year

nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - nascimento

if idade <= 9:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JUNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'

print(f'O atleta tem {idade} anos.')
print(f'Classificação: {classificacao}')
