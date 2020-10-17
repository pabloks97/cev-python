# Exercício 057 - Validação de Dados

sexo = input('Informe seu sexo [M/F]: ')
while sexo not in 'MFmf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')
print(f'Sexo {sexo.upper()} registrado com sucesso!')
