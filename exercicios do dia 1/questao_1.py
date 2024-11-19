#Questão 1
nota1 = int( input('Insira a sua primeira nota semestral: '))
nota2 = int( input('Insira a sua segunda nota semestral: '))
nota3 = int( input('Insira a sua terceira nota semestral: '))

soma = nota1 + nota2 + nota3
media = soma / 3

print('Sua média é: {:.1f}'.format (media))
