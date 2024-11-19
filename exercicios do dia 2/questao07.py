cont = 0 

for i in range (8):
    notas = int(input(f'insira a {i+1}º nota: '))
    if notas >= 0 and notas <= 100:
        cont+= 1

print(f'foram validadas {cont} notas para o SUAP')
