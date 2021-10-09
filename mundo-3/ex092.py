# Exercício 092 - Cadastro de Trabalhador em Python

from cev.utils import calcula_idade
from datetime import datetime

ano_atual = datetime.now().year

dicio = {}
dicio['nome'] = input('Nome: ')
dicio['idade'] = calcula_idade(int(input('Ano de Nascimento: ')))
dicio['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicio.get('ctps') > 0:
    dicio['contratação'] = int(input('Ano de Contratação: '))
    dicio['salário'] = float(input('Salário: '))
    dicio['aposentadoria'] = dicio['idade'] + ((dicio['contratação'] + 35) - ano_atual)
print(20 * '-=')

for k, v in dicio.items():
    print(f' - {k} tem o valor {v}')
