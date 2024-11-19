total = 5
idade_maior = 0
idade_menor = 500

for i in range(total):
    idade = int(input('digite a idade: '))
    if idade > idade_maior:
        idade_maior = idade
    elif idade < idade_menor:
        idade_menor = idade
    
print(f'a idade maior é: {idade_maior}')
print(f'a idade menor é: {idade_menor}')