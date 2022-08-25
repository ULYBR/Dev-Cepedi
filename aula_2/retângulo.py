if __name__ == '__main__':
    #crie um programa que faz o calculo da area de um rentângulo.
    x_sup = float(input('P1 x:'))
    y_sup = float(input('P1 y:'))
    x_inf = float(input('P2 x:'))
    y_inf = float(input('P2 y:'))
    base= abs((x_inf - x_sup))
    altura = abs((y_sup - y_inf))
    area = base * altura
    print(f'Área:{area:.2f}')


