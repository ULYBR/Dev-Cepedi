#faça um programa que  Contador de vogais.
if __name__ == "__main__":
    def conta_vogais(string):
        string = string.lower()  # para que a comparação não seja sensível a maiuscula/minuscula
        vogais = 'aeiou'
        return {i: string.count(i) for i in vogais if i in string}

    text = input('digite um texto: ')
    print(conta_vogais(f'{text}'))