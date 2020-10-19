# Exercício 080 - Lista Ordenada Sem Repetições

valores = []
for n in range(5):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0 or valor > max(valores):
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for i,v in enumerate(valores):
            if valor < v:
                valores.insert(i, valor)
                print(f'Adicionado na posição {i} da lista...')
                break
print(f'Os valores digitados em ordem foram {valores}')
