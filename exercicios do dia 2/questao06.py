print('digite seis números para calcular a média:')

soma = 0
total = 6
for i in range(total):
   nota = int(input(f'{i+1}º nota : '))
   soma = soma + nota

media = soma / total
print(f'a média é: {media:.2f}')
