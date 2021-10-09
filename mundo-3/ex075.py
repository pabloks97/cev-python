# Exercício 075 - Análise de Dados em uma Tupla

from cev.utils import par, posicao

perguntas = ['um', 'outro', 'mais um', 'o último']
lista = []
for n in range(len(perguntas)):
    lista.append(int(input(f'Digite {perguntas[n]} número: ')))

valores = tuple(lista)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')

posicao_do_tres = posicao(3, valores)
if posicao_do_tres < 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {posicao_do_tres}ª posição')

pares = [n for n in valores if par(n)]
print(f'Os valores pares digitados foram {pares}')
