#Escreva um programa que:
#• Leia uma matriz quadrada de ordem 30 contendo números inteiros;
#• Gere e imprima um vetor que deverá conter os elementos da diagonal #principal da matriz;
#• Gere e imprima um vetor que deverá conter os elementos da diagonal #secundária da matriz.
import random
m = []

for l in range(30):
    linha = []
    for c in range(30):
        linha.append(random.randint(1,50))
    m.append(linha)

d_principal= []
d_secundario= []

for i in range(((30*30)-30)):
    d_principal.append(m[i][i])
print(d_principal)
for l in range(29,-1,-1):
    for c in range(30):
        d_secundario.append(m[l][c])
print(d_secundario)

#FALTA TERMINAAARRRRRR