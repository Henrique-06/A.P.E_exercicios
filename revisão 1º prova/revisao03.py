
cupom = 30
saldo = 0
vendas = 0 
total_compra = 0
total_cupom = 0
maior_venda = -1
maior_cupom = -1


while True:
    compra = float(input('valor da compra: '))

    if compra == -1:
        break
    vendas += 1
    total_compra += compra
    saldo += compra

    if compra > maior_venda:
        maior_venda = compra

    qtd_cupom = int(compra / cupom)
    if qtd_cupom > maior_cupom:
        maior_cupom = qtd_cupom

    saldo = (saldo % cupom)
    
    nv_cupom = (cupom - saldo)
    
    if compra < cupom:
        print('sem cupons')
    else:
        print(f'{qtd_cupom} cupons')
    

    print(f'R$ {saldo:.2f} de saldo')
    print(f'R${nv_cupom:.2f} para um novo cupom')


print(f'total de vendas: {vendas}')
print(f'R${total_compra:.2f} arrecadado')
print(f'{total_cupom} cupons totais')
print(f'maior valor vendido: {maior_venda}, quantidade de cupons entregue: {maior_cupom}')
