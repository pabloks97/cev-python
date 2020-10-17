# Exercício 039 - Alistamento Militar

from datetime import datetime

nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year

idade = ano_atual - nascimento
alistamento = nascimento + 18

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {alistamento}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
