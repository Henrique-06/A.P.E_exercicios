TOTAL=6
idade_maior = -1
idade_menor = 200
for i in range(TOTAL):
    idade = int(input(f'{i+1} idade: '))
    if idade > idade_maior:
        idade_maior = idade
    if idade < idade_menor:
        idade_menor = idade

print(f'a maior idade foi: {idade_maior}')
print(f'a menor idade foi: {idade_menor}')
