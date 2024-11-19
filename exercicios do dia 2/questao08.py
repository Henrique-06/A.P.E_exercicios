cashback = 0
compras_do_dia = 0
total = 400

for i in range(total):
    total_compra = float(input('valor da compra: '))
    
    compras_do_dia += total_compra
    if total_compra <= 100:
        cashback += (total_compra*0.04)
    elif total_compra <= 200:
        cashback += (total_compra*0.06)
    elif total_compra <= 400:
        cashback += (total_compra*0.08)
    else:
        cashback += (total_compra*0.1)
        

print(f'valor total arrecadado: {compras_do_dia}')
print(f' cash gerado: {cashback:.2f}') 


