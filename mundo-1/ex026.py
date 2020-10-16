# Exercício 026 - Primeira e Última Ocorrência de Uma String

frase = input('Digite uma frase: ').strip().lower()

letras_a = frase.count('a')
print(f'A letra A aparece {letras_a} vezes na frase.')

primeiro_a = frase.find('a') + 1
print(f'A primeira letra A apareceu na posição {primeiro_a}')

último_a = frase.rfind('a') + 1
print(f'A última letra A apareceu na posição {último_a}')
