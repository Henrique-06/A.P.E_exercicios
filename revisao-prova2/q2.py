#Escreva um programa que:
#• Leia uma matriz M de ordem 20 x 50 contendo valores inteiros;
#• Leia um valor inteiro K;
#• Imprima todas as posições (linha e coluna) em que se encontra o valor #K dentro da matriz M.
import random

m = []

for l in range(20):
    linha = []
    for c in range(50):
        linha.append(random.randint(1,50))
        m.append(linha)

k = int(input('digite um valor: '))

for l in range(20):
    for c in range(50):
        if m[l][c] == k:
            print( l,c)