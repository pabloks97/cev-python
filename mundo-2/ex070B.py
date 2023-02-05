# Exercício 070 - Estatísticas em Produtos


class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco


def main():
  produtos = []
  while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    novo_produto = Produto(nome, preco)
    produtos.append(novo_produto)

    resposta = input('Quer continuar? [S/N] ')
    if resposta not in 'sS': break
  print(f'{" FIM DO PROGRAMA ":-^40}')

  total_compra = sum([p.preco for p in produtos])
  acima_de_mil = len([p for p in produtos if p.preco > 1000])
  mais_barato = min(produtos, key=lambda p: p.preco)

  print(f'O total da compra foi R${total_compra:.2f}')
  print(f'Temos {acima_de_mil} produtos custando mais de R$1000.00')
  print(f'O produto mais barato foi {mais_barato.nome} que custa R${mais_barato.preco:.2f}')    


# ----------------------------------------
if __name__ == '__main__':
    main()
