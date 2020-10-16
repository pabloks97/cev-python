# Exercício 022 - Analisador de Textos

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

letras = nome.replace(' ', '')
print(f'Seu nome tem ao todo {len(letras)} letras')

primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} ', end='')
print(f'e ele tem {len(primeiro_nome)} letras')
