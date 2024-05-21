valor_cambio = 0
total_billete_mil = 50000
total_billete_dosmil = 60000
total_billete_cincomil = 150000
total_stock = total_billete_cincomil + total_billete_dosmil + total_billete_mil

while valor_cambio <= total_stock:
    cont_mil = 0
    cont_dosmil = 0
    cont_cincomil = 0

    try:
        valor_cambio = int(input("""
            Ingresa cantidad a cambiar.
            Recuerda que debes ingresar un monto superior a $10.000 y múltiplos de 1000:  
            """))
    except Exception as err:
        print(err)

    cont = valor_cambio
    
    print(total_stock)

    if valor_cambio <= total_stock:
        if valor_cambio >= 10000 and valor_cambio % 1000 == 0:

            #Validacion billetes cinco mil
            if (cont <= total_billete_cincomil or cont <= total_stock):
                for e in range(5000, cont + 1, 5000):
                    if total_billete_cincomil >= 5000:
                        total_billete_cincomil -= 5000
                        cont_cincomil += 1
                        cont -= 5000
                print(f'{cont_cincomil} billetes de $5000')
            
            #Validacion billetes dos mil
            if cont <= total_billete_dosmil or cont <= total_stock:
                for e in range(2000, cont + 1, 2000):
                    if total_billete_dosmil >= 2000:
                        total_billete_dosmil -= 2000
                        cont_dosmil += 1
                        cont -= 2000
                print(f'{cont_dosmil} billetes de $2000')
            
            #Validacion billetes mil
            if cont <= total_billete_mil or cont <= total_stock:
                for e in range(1000, cont + 1, 1000):
                    if total_billete_mil >= 1000:
                        total_billete_mil -= 1000
                        cont_mil += 1
                        cont -= 1000
                print(f'{cont_mil} billetes de $1000')
            
            
    else:
        print('Monto ingresado supera stock.')
        break
    


#def descontando_cincomil():
