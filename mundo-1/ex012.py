# Exercício 012 - Calculando Descontos

preco = float(input('Qual é o preço do produto? R$'))
desconto = 0.05 * preco
total = preco - desconto

print(f'O produto que custava R${preco:.2f}, ', end='')
print(f'na promoção com desconto de 5% vai custar R${total:.2f}')
