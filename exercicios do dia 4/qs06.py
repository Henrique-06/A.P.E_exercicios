# Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
# O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade
# média deste grupo de indivíduos.
# Entrada
# A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo
# for lido.
# Saída
# A saída contém um valor correspondente à média de idade dos indivíduos.
# A média deve ser impressa com dois dígitos após o ponto decimal.


idd_total = 0
idd_soma = 0

while True:
    idade = int(input('digite idade: '))
    if idade < 0:
        break
    else:
        idd_soma += idade
        idd_total += 1

print(f'{(idd_soma/idd_total):.2f}')