num= int (input ('digite um número: '))

fatorial = 1

for i in range(1,num+1):
    fatorial *= i

print(f'{num}! = {fatorial}')
