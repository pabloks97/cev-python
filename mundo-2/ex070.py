# Exercício 070 - Estatísticas em Produtos

def main():
    total = mais_de_mil = 0
    nome_mais_barato = ''
    preço_mais_barato = 0

    while True:
        nome, preço = compra_produto()
        total += preço
        if preço > 1000:
            mais_de_mil += 1
        if preço < preço_mais_barato or preço_mais_barato == 0:
            nome_mais_barato = nome
            preço_mais_barato = preço    
        if not continua():
            break

    print(f'{" FIM DO PROGRAMA ":-^40}')
    print(f'O total da compra foi R${total:.2f}')
    print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {nome_mais_barato} que custa R${preço_mais_barato:.2f}')


def continua():
    '''Retorna True se o usuário quer continuar.'''
    return input('Quer continuar? [S/N] ') in 'sS'

def compra_produto():
    '''Retorna nome e preço do produto.'''
    nome = input('Nome do Produto: ')
    preço = float(input('Preço: R$'))
    return nome, preço


# ----------------------------------------
main()
