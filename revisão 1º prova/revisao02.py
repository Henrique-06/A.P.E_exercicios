
cupom = 30
saldo = 0


while True:
    compra = float(input('valor da compra: '))
    saldo += compra
    qtd_cupom = int(compra / cupom)
    saldo = (saldo % cupom)
    nv_cupom = (cupom - saldo)
    if compra < cupom:
        print('sem cupons')
    else:
        print(f'{qtd_cupom} cupons')
    
    print(f'R$ {saldo:.2f} de saldo')
    print(f'R${nv_cupom:.2f} para um novo cupom')

 
