# Módulo dado do pacote cev


def le_int(prompt='', erro=''):
    '''Lê um número inteiro do usuário. le_int() -> int'''
    return valida(prompt, erro, int)


def le_float(prompt='', erro=''):
    '''Lê um número real do usuário. le_float() -> float'''
    return valida(prompt, erro, float)


def le_dinheiro(prompt='', erro=''):
    '''Lê um valor monetário do usuário. le_dinheiro() -> float'''
    return valida(prompt, erro, lambda x: float(x.replace(',', '.')))


def valida(prompt, erro, tipo):
    '''
    Retorna um dado do usuário, se for do tipo passado.
    valida(string, string, tipo) -> tipo
    '''
    while True:
        try:
            x = tipo(input(prompt))
        except (ValueError, TypeError):
            print(erro)
        except KeyboardInterrupt:
            print('\nInterrompido pelo usuário.')
            return 0
        else:
            return x
