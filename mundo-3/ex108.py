# Exercício 108 - Formatando Moedas em Python

from moeda import moeda, metade, dobro, aumenta

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preço)} é {moeda(metade(preço))}')
print(f'O dobro de {moeda(preço)} é {moeda(dobro(preço))}')
print(f'Aumentando 10%, temos {moeda(aumenta(10, preço))}')
