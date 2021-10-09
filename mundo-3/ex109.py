# Exercício 109 - Formatando Moedas em Python

from cev.moeda import moeda, metade, dobro, aumenta

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(aumenta(10, preco))}')
