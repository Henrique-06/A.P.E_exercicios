cont_sim = cont_nao = cont_inv = 0
total = 5

for i in range (total):
    voto = str(input('vote sim ou nao: '))
    if voto == 'sim':
        cont_sim += 1
    elif voto == 'nao':
        cont_nao += 1
    else:
        cont_inv += 1

print(f'total de votos sim: {cont_sim/total*100}%')
print(f'total de votos nao: {cont_nao/total*100}%')
print(f'total de votos inválidos: {cont_inv/total*100}%')



