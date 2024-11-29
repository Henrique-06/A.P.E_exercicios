n1 = int(input('digite um valor: ')) 
n2 = int(input('digite outro valor: ')) 

while n1 != n2:
    if n1 > n2:
        print('ordem decrescente')
    else:
        print('ordem crescente')
        #lendo os próximos valores
    n1 = int(input('digite um valor: '))
    n2 = int(input('digite outro valor: ')) 

print('fim, são iguais')

#tem a opção while True com if elif e else

# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
# mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
# Entrada
# A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser
# encerrada ao ser fornecido valores iguais para X e Y.
# Saída
# Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso
# contrário imprima a mensagem “Decrescente”.