# Exercício 107 - Exercitando Módulos em Python

from moeda import metade, dobro, aumenta

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço:.1f} é R${metade(preço):.1f}')
print(f'O dobro de R${preço:.1f} é R${dobro(preço):.1f}')
print(f'Aumentando 10%, temos R${aumenta(10, preço):.1f}')
