# Exercício 114 - Site Está Acessível?

import urllib.request

url = 'https://' + input('Digite o endereço do site: ')

try:
    urllib.request.urlopen(url)
except:
    print('Erro! O site está inacessível.')
else:
    print('O site está acessível!')
