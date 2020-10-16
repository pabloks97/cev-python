# Exercício 011 - Pintando Parede

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

área = largura * altura

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {área}m².')
print(f'Para pintar essa parede, você precisará de {(área / 2):.4f}l de tinta.')
