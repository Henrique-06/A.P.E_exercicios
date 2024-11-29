import random

menor,maior = 1,100
SECRETO = random.randint(menor,maior)
qtd_erros = 0


while True:
    num = int(input(f'número{menor,maior}: '))

    while num>maior or num<menor: # ele verifica se está dentro da faixa=>
        print('vc saiu da faixa,tente de novo ')
        qtd_erros += 1
        num = int(input(f'número{menor,maior}: '))

    if (num == SECRETO): #se ele acertar, e se é maior ou menor=>
         break
    if num > SECRETO:
        print('seu número é maior ')
        maior = num -1
    else:
        print('seu número é menor')
        menor = num +1
        
    qtd_erros += 1
    if (qtd_erros == 5):
        break

if (num == SECRETO):
    print(f' você acertou!!')
    print(f' nº de tentativas: {qtd_erros}')
else:
    print('você esgotou a quantidade de tentativas')
