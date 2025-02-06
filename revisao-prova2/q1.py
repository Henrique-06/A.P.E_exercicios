#Escreva um programa que:
#• Leia um valor inteiro N;
#• Leia um vetor A contendo N inteiros;
#• Gere e imprima um vetor B onde cada elemento de B será calculado com base no elemento de A
#da mesma posição usando a seguinte regra: se o elemento de A for par, o elemento de B será 0,
#e se o elemento de A for ímpar, o elemento de B será 1.
#Exemplo: N = 8, A = [7, 12, 15, 10, 4, 9, 3, 6], B = [1, 0, 1, 0, 0, 1, 1, 0]
import random

vetor_a=[]
vetor_b=[]
n= int(input('valor: '))

for i in range(n):
    vetor_a.append(random.randint(1,100))
    if (vetor_a[i] % 2) == 0:
        vetor_b.append(0)
    else:
        vetor_b.append(1)



print(f'A = {vetor_a}')
print(f'B = {vetor_b}')
