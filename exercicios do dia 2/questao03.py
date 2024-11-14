
n = int(input('Qual numero vc quer saber o múltiplo?: '))
x = int(input('agora, digite um numero para a faixa inicial: '))
y = int(input(f'agora, digite um numero para a faixa final: '))

# exemplo range (2, )
for m in range(x,y+1):
    if m%n==0: 
        print(f'{m}',end=' ')
