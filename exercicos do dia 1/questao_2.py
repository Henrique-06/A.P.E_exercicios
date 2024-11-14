#Questão 2
aulas = int ( input('Insira a quantidade de aulas de sua diciplina: '))
faltas = int ( input('Agora, insira a quantidade de faltas de um aluno: '))

passo1 = (faltas*100) / aulas
freq = 100 - passo1

print(' A frenquência do aluno é de: {:.1f}%'.format(freq)) 
