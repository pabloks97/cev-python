# Exercício 097 - Um Print Especial

def escreve(texto, estilo='~', preenchimento=4):
    tamanho = len(texto) + preenchimento
    print(tamanho * estilo)
    print(f'{texto:^{tamanho}}')
    print(tamanho * estilo)

escreve('Gustavo Guanabara')
escreve('Curso de Python no YouTube')
escreve('CeV')
