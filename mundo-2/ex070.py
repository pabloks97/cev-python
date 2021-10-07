# Exercício 070 - Estatísticas em Produtos


def main():
    total = mais_de_mil = 0
    nome_mais_barato = ''
    preco_mais_barato = 0

    while True:
        nome, preco = compra_produto()
        total += preco
        if preco > 1000:
            mais_de_mil += 1
        if preco < preco_mais_barato or preco_mais_barato == 0:
            nome_mais_barato = nome
            preco_mais_barato = preco
        if not continua():
            break

    print(f'{" FIM DO PROGRAMA ":-^40}')
    print(f'O total da compra foi R${total:.2f}')
    print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato:.2f}')


def continua():
    '''Retorna True se o usuário quer continuar.'''
    return input('Quer continuar? [S/N] ') in 'sS'


def compra_produto():
    '''Retorna nome e preço do produto.'''
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    return nome, preco


# ----------------------------------------
if __name__ == '__main__':
    main()
