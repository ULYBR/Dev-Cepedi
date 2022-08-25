if __name__ == '__main__':
    x_c = float(input('centro Xc: '))
    y_c = float(input('centro Yc: '))
    raio  = float(input('Raio: '))
    x_p = float(input('Xp: '))
    y_p = float(input('Yp: '))
    distancia = ((x_p - x_c)**2 + (y_p - y_c)**2)**5

    resposta = 'pertence' if distancia <= raio else 'não pertence'

    mensagem = (f'({x_p}.{y_p}) {resposta} pertence à circunferência ({x_c},{y_c}, {raio})')

    print (mensagem)


