cont=0
total= 8
for i in range(total):
    notas= int(input(f'Adicione a nota do {i+1}º estudante: '))
    if notas <=100 and notas>=0:
        cont+=1
print(f'foram informadas {cont} notas válidas para o Suap')
 
