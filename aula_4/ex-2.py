#faça um códico que seja um Palíndromo.
if __name__ == "__main__":
    text = str(input('Digite um texto: '))
    if str(text) == str(text) [::-1]:
        print(f'O texto: {text} é um Palíndromo : {text[::-1]}')
    else :
        print(f'O texto: {text} não é Palíndromo : {text[::-1]}')
