print('digite seis números para calcular a média:')

soma = 0

for i in range(6):
   nota = int(input(f'{i+1}º nota : '))
   soma = soma + nota

media = soma / 6
print(f'a média é: {media:.2f}')
