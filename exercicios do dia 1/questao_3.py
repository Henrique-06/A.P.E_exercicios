#Questão 3
ms = int ( input (' Insira aqui a sua Média Semestral: '))
nf = int ( input (' Agora, insira a sua Nota Final: '))

media = ((ms*6) + ( nf*4)) /10

print(f' A sua Média Final é: {media}',)

if media >= 50:
    print('Parabéns!! Você foi aprovado(a)!!')
else:
    print('Que pena!! Você foi REPROVADO(A)!!')
