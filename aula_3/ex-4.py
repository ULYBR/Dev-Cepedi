if __name__ == "__main__":

    salario = float(input('Digite o seu Sálario Bruto: '))


    if   salario < 1903.99:
        imposto = 0
    elif salario < 2826.65:
        imposto = salario * 0.075

    elif salario < 3751.06:
        imposto = salario * 0.15
    elif salario < 4664.69:
        imposto = salario * 0.225
    else:
        imposto = salario * 0.275

    print(f'Sálario líquido: {salario - imposto}')

