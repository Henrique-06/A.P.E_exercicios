num = int(input('digite um número: '))

soma = 0

for i in range (1,num+1):
    soma += (1 / i)

print(f'a soma é:{soma:.2f} ')
