# Exercício 044 - Gerenciador de Pagamentos

from utils import exibe_menu, desconto, juros

OPÇÕES = ['à vista dinheiro/cheque',
          'à vista cartão',
          '2x no cartão',
          '3x ou mais no cartão']

preço = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
exibe_menu(OPÇÕES)
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = desconto(10, preço)
elif opção == 2:
    total = desconto(5, preço)
elif opção == 3:
    total = preço
    print(f'Sua compra será parcelada em 2x de R${(total / 2):.2f}')
elif opção == 4:
    total = juros(20, preço)
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = total / parcelas
    print(
        f'Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f} COM JUROS')
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
