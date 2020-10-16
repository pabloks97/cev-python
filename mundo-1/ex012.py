# Exercício 012 - Calculando Descontos

from utils import porcento

preço = float(input('Qual é o preço do produto? R$'))
desconto = porcento(5, preço)
total = preço - desconto

print(f'O produto que custava R${preço:.2f}, na promoção', end=' ')
print(f'com desconto de 5% vai custar R${total:.2f}')
