# Exercício 014 - Conversor de Temperaturas


def main():
    c = float(input('Informe a temperatura em °C: '))
    f = fahrenheit(c)
    print(f'A temperatura de {c}°C corresponde a {f}°F!')


def fahrenheit(celsius):
    '''Converte temperatura em Celsius para Fahrenheit.'''
    return (celsius - (0.1 * celsius)) * 2 + 32


# -----------------------------------------
if __name__ == '__main__':
    main()
