# Exercício 026 - Primeira e Última Ocorrência de Uma String

frase = input('Digite uma frase: ').strip().upper()
letra = input('Digite uma letra: ').strip().upper()

letras = frase.count(letra)
print(f'A letra {letra} aparece {letras} vezes na frase.')

primeira = frase.find(letra) + 1
print(f'A primeira letra {letra} apareceu na posição {primeira}')

ultima = frase.rfind(letra) + 1
print(f'A última letra {letra} apareceu na posição {ultima}')
