# Exercício 032 - Ano Bissexto

from datetime import datetime
from utils import é_bissexto

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.now().year

resultado = '' if é_bissexto(ano) else ' NÃO'
print(f'O ano {ano}{resultado} é BISSEXTO')
