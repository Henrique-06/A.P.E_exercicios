cont= 0
for k in range(6):
    a = int(input('digite o 1º lado: '))
    b = int(input('digite o 2º lado: '))
    c = int(input('digite o 3º lado: '))

    if a<b+c and b<a+c and c<a+b:
        cont=cont+1
print(f'{cont} medidas foram validadas')


