if __name__ == '__main__':
    #crie um programa que faz o calculo do imc .
    peso = float(input('digite seu peso : '))
    altura = float(input("digite sua altura: "))

    imc = peso / altura**2

    print(f'IMC:{imc:.2f}')
