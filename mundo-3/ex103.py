# Exercício 103 - Ficha do Jogador

def main():
    nome = input('Nome do Jogador: ')
    gols = input('Número de Gols: ')
    gols = int(gols) if gols.isnumeric() else 0 
    ficha(nome, gols) if len(nome) else ficha(gols=gols)


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# --------------------------------
main()
