# Exercício 075 - Análise de Dados em uma Tupla

from utils import é_par, posição

perguntas = ['um', 'outro', 'mais um', 'o último']
lista = []
for n in range(len(perguntas)):
    lista.append(int(input(f'Digite {perguntas[n]} número: ')))

valores = tuple(lista)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')

posição_do_três = posição(3, valores)
if posição_do_três < 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {posição_do_três}ª posição')

pares = [n for n in valores if é_par(n)]
print(f'Os valores pares digitados foram {pares}')
