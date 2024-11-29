total_cash = 0
for i in range(5):
    valor = float(input('valor da compra: '))
    if valor<= 100:
        cash = valor*0.04
    elif valor<=200:
        cash = valor*0.06
    elif valor<=400:
        cash = valor*0.1
    else:
        cash = valor*0.90
    total_cash += cash

print(f'total do cash: {total_cash}')
    
    

    

    
