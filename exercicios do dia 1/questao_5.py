#Questão 5
alunos_aprovados = int(input(' Insira a quantidade de alunos aprovados: '))
alunos_reprovados = int(input(' Insira a quantidade de alunos reprovados: '))

alunos_totais = (alunos_aprovados + alunos_reprovados)

porcentagem = ((alunos_aprovados * 100) / alunos_totais)

print(' Porcentagem de alunos aprovados: {:.1f}%'.format(porcentagem))
