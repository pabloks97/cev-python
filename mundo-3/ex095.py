# Exercício 095 - Aprimorando os Dicionários

time = []
while True:
    jogador = {'nome': input('Nome do Jogador: ')}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = [int(input(f'\tQuantos gols na partida {i+1}? ')) for i in range(partidas)]
    jogador['gols'] = gols
    time.append(jogador)
    if input('Quer continuar? ') in 'Nn': break

print(25 * '-=')
print(f'{"cod":>3} {"nome":<15} {"gols":<15} {"total":<5}')
print(45 * '-')
for i, j in enumerate(time):
    nome = j["nome"]
    gols = str(j["gols"])
    total = sum(j["gols"])
    print(f'{i:>3} {nome:<15} {gols:<15} {total:<5}')
print(45 * '-')

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999: break
    if cod > len(time) - 1:
        print(f'ERRO! Não existe jogador com código {cod}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}:')
        gols = time[cod]['gols']
        for i, g in enumerate(gols):
            print(f'\tNo jogo {i+1} fez {g} gols.')
    print(45 * '-')
print('<< VOLTE SEMPRE >>')
