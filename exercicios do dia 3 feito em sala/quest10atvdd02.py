total_sim= total_nao = total_invalido= 0
total = 5
for i in range(total):
    voto = input('digite sim ou nao: ')
    if voto== 'sim':
        total_sim+=1
    elif voto=='não':
        total_nao+=1
    else:
        total_invalido+=1

percentual_sim= (100*total_sim)/80
percentual_nao= (100*total_nao)/80
percentual_invalido= (100*total_invalido)/80


print(f'foram')
