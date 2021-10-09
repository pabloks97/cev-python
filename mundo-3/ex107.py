# Exercício 107 - Exercitando Módulos em Python

from cev.moeda import metade, dobro, aumenta

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.1f} é R${metade(preco):.1f}')
print(f'O dobro de R${preco:.1f} é R${dobro(preco):.1f}')
print(f'Aumentando 10%, temos R${aumenta(10, preco):.1f}')
