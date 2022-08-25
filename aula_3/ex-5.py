import datetime as dt

if __name__ == '__main__':

    data = input('Data (dd/mm/aaaa):')
    data = dt.datetime.strptime(data, '%d/%m/%Y')

    dia, mes = data.day, data.month

    if mes == 1 or mes == 2:
        estacao = 'Verão'
    elif mes == 3:
        if dia < 20:
            estacao = 'Verão'
        else :
            estacao = 'Outono'
    elif mes == 4 or mes == 5 :
        if dia < 21 :
            estacao = 'Outono'
        else:
            estacao = 'Inverno'
    elif mes == 6 :
        if dia < 21 :
            estacao = 'Outono'
        else :






    print(f"{data.strptime('%d/%m/%Y')}")


