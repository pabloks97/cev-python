# Módulo dado do pacote cev

def lê_int(prompt='', erro=''):
    '''Lê um número inteiro do usuário. lê_int() -> int'''
    return valida(prompt, erro, int)


def lê_float(prompt='', erro=''):
    '''Lê um número real do usuário. lê_float() -> float'''
    return valida(prompt, erro, float)


def lê_dinheiro(prompt='', erro=''):
    '''Lê um valor monetário do usuário. lê_dinheiro() -> float'''
    return valida(prompt, erro, lambda x: float(x.replace(',', '.')))


def valida(prompt, erro, tipo):
    '''
    Retorna um dado do usuário, se for do tipo passado.
    valida(string, string, tipo) -> tipo
    '''
    while True:
        try: x = tipo(input(prompt))
        except (ValueError, TypeError):
            print(erro)
        except KeyboardInterrupt:
            print('\nInterrompido pelo usuário.')
            return 0
        else: return x
