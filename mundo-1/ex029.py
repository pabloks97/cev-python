# Exercício 029 - Radar Eletrônico


def main():
    velocidade = int(input('Qual é a velocidade atual do carro? '))

    if velocidade > 80:
        multa = calcula_multa(velocidade)
        print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
        print(f'Você deve pagar uma multa de R${multa:.2f}')

    print('Tenha um bom dia! Dirija com segurança!')


def calcula_multa(v):
    '''Retorna o valor da multa de acordo com a velocidade.'''
    return (v - 80) * 7


# --------------------------------
if __name__ == '__main__':
    main()
