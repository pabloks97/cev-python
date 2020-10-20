# Exercício 093 - Cadastro de Jogador de Futebol

jogador = {}
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador.get("nome")} jogou? '))
gols = []
for p in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = gols
jogador['total'] = sum(jogador.get('gols'))

print(30 * '-=')
print(jogador)

print(30 * '-=')
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')

print(30 * '-=')
print(f'O jogador {jogador.get("nome")} jogou {len(jogador.get("gols"))} partidas.')
for i, v in enumerate(jogador.get('gols')):
    print(f'\t=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador.get("total")} gols.')
