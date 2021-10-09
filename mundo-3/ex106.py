# Exercício 106 - Sistema Interativo de Ajuda em Python

while True:
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM': break
    help(comando)
