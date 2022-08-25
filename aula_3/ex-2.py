if __name__ == "__main__":
    n = int(input('Valor: '))
    intervalo = [(0, 25)],[(25, 50)],[(50, 75)],[(75, 100)]

    if n <= 0 or n <= 100:
        print(f'{n} pertence ao intervalo {intervalo}')
    else:
        print(f'Valor inválido: {n} não pertence ao intervalo [0, 100]')