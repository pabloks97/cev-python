# Exercício 088 - Palpites para a Mega Sena

from random import sample
from utils import escreve

escreve('JOGA NA MEGA SENA', preenchimento=16)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(3*'-=', f'SORTEANDO {jogos} JOGOS', 3*'=-')
números = [n for n in range(1, 61)]
palpites = [sample(números, 6) for i in range(jogos)]
for i, p in enumerate(palpites):
    print(f'Jogo {i+1}: {p}')
print(5*'-=', f'< BOA SORTE! >', 5*'=-')
