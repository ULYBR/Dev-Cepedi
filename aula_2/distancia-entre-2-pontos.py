if __name__ == '__main__':
    x_1 = float(input("X1:"))
    y_1 = float(input("Y1:"))
    x_2 = float(input("X2:"))
    y_2 = float(input("Y2:"))

    distancia = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    print(f'Distância entre ({x_1} , {y_1}) e ({x_2}, {y_2}): {distancia:.2f}')
