# Exercício 014 - Conversor de Temperaturas

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = ((celsius - (0.1 * celsius)) * 2 + 32)
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F!')
