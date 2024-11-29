
maior,menor = (10,0)
while True:
    n1 = float(input('1º nota: '))
    while n1 > maior or n1 < menor:
        print('nota inválida')
        n1 = float(input('1º nota: '))
    
    n2 = float(input('2º nota: '))
    while n2 > maior or n2 < menor:
        print('nota inválida')
        n2 = float(input('1º nota: '))
    
    print(f'média= {((n1 + n2)/2):.2f}')
    







# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema

# cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo

# menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida,
# conforme o exemplo.