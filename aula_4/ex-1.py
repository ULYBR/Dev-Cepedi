#faça um programa que imprime tanto ele quanto inverso dele
if __name__ == "__main__":
    text =str(input('Digite um texto: '))
    invtext = text[::-1]

    print(f'O inverso do texto{text} foi {invtext}')

