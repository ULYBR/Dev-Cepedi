if __name__ == '__main__':
    n = int(input('Digite um número: '))
    d = int(input('Digite segundo número: '))

    if n % d == 0:
        print(f'{n} é múltiplo de {d}.')
    else:
        print(f'{n} não é múltiplo de {d}')

