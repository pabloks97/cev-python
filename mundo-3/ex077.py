# Exercício 077 - Contando Vogais em Tupla


def main():
    palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
                'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
                'programar', 'futuro')

    for p in palavras:
        print(f'Na palavra {p.upper()} temos ', end='')
        [print(letra, end=' ') for letra in p if vogal(letra)]
        print()


def vogal(letra):
    '''Retorna True se letra for uma vogal.'''
    return len(letra) == 1 and letra in 'AaEeIiOoUu'


# ----------------------------------------
if __name__ == '__main__':
    main()
