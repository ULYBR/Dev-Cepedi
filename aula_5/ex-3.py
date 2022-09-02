if __name__ == "__main__":
    import json
    with open('datasets/frase.txt','r',encoding='utf-8') as fd:
        frases = [
            frase for frase in fd.read().split('\n')if frase != ''
        ]

        print(frases)


        indice_invertido = {palavra: set() for frase in frases for palavra in frase.split()}

        for frase_id, frase in enumerate(frases):
           for palavra in frase.split():
                indice_invertido[palavra].add(frase_id)

        print(indice_invertido)



        query = input('query: ').split()
        print(query)
        resultado =set()
        for termo in query:
            resultado = resultado.union(indice_invertido[termo])

        for frase_id in resultado:
            print(frases[frase_id])







