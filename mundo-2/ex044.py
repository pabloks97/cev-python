# Exercício 044 - Gerenciador de Pagamentos

from cev.menu import exibe_opcoes
from cev.utils import desconto, juros

OPCOES = [
    'à vista dinheiro/cheque', 'à vista cartão', '2x no cartão',
    '3x ou mais no cartão'
]

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
exibe_opcoes(OPCOES)
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = desconto(10, preco)
elif opcao == 2:
    total = desconto(5, preco)
elif opcao == 3:
    total = preco
    print(f'Sua compra será parcelada em 2x de R${(total / 2):.2f}')
elif opcao == 4:
    total = juros(20, preco)
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
