if __name__ == '__main__':
    valor = int(input('Valor em R$: '))

    quantidade_200 = valor // 200
    valor %= 200
    quantidade_100 = valor // 100
    valor %= 100
    quantidade_50 = valor // 50
    valor %=50
    quantidade_20 = valor // 20
    valor %=20
    quantidade_10 = valor // 10
    valor %= 10
    quantidade_5 = valor // 5
    valor %= 5
    quantidade_2 = valor // 2
    valor %= 2
    quantidade_1 = valor // 1
    valor %= 1

    print(f'{quantidade_200} nota(s) de R$ 200,00')
    print(f'{quantidade_100} nota(s) de R$ 100,00')
    print(f'{quantidade_50} nota(s) de R$ 50,00')
    print(f'{quantidade_20} nota(s) de R$ 20,00')
    print(f'{quantidade_10} nota(s) de R$ 10,00')
    print(f'{quantidade_5} nota(s) de R$ 5,00')
    print(f'{quantidade_2} nota(s) de R$ 2,00')
    print(f'{quantidade_1} moeda(s) de R$ 1,00')

