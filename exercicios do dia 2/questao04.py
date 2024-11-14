
n = int(input('Qual numero vc quer saber o múltiplo?: '))
x = int(input('agora, digite um numero para a faixa inicial: '))
y = int(input(f'agora, digite um numero para a faixa final: '))

cont = 0
for m in range(x,y+1):
    if m%n==0:
        cont = cont+1
print(f'{cont}',end=' ')
