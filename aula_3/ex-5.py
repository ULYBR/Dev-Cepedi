import datetime as dt
#
# if __name__ == '__main__':
#
#     data = input('Data (dd/mm/aaaa):')
#     data = dt.datetime.strptime(data, '%d/%m/%Y')
#
#     dia, mes = data.day, data.month
#
#     if mes == 1 or mes == 2:
#         estacao = 'Verão'
#     elif mes == 3:
#         if dia < 20:
#             estacao = 'Verão'
#         else :
#             estacao = 'Outono'
#     elif mes == 4 or mes == 5 :
#         if dia < 21 :
#             estacao = 'Outono'
#         else:
#             estacao = 'Inverno'
#     elif mes == 6 :
#         if dia < 21 :
#             estacao = 'Outono'
#         else :
#             estacao = 'Inverno'
#     elif mes == 7 or mes == 8:
#         estacao = 'Inverno'
#     elif mes == 9 :
#         if dia < 22 :
#             estacao = 'Inverno'
#         else :
#             estacao = 'Primavera'
#     elif mes == 10 or mes == 11 :
#         estacao = 'Primavera'
#     elif mes == 12 :
#         if dia < 21 :
#             estacao = 'Primavera'
#         else :
#             estacao = 'Verão'
#
#
#
#
#
#
#     print(f"{data.strftime('%d/%m/%Y')} {estacao}")
#
# outra maneira >>>

if __name__ == '__main__':


    data = input('Data (dd/mm/aaaa): ')
    data = dt.datetime.strptime(data, '%d/%m/%Y').date()

    dia, mes = data.day, data.month
    inicio_outono = dt.date(data.year, 3, 20)
    inicio_inverno = dt.date(data.year, 6, 21)
    inicio_primavera = dt.date(data.year, 9, 22)
    inicio_verao = dt.date(data.year, 12, 21)

    if data < inicio_outono:
        estacao = 'Verão'
    elif data < inicio_inverno:
        estacao = 'Outono'
    elif data < inicio_primavera:
        estacao = 'Inverno'
    elif data < inicio_verao:
        estacao = 'Primavera'
    else:
        estacao = 'Verão'

    print(f"{data.strftime('%d/%m/%Y')} é {estacao}")

