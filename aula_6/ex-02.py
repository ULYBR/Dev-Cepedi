# Exercício 2: Criar nova lista sem duplicatas
# input:
# itens: list[int] = Lista de inteiros com valores repetidos
# output:
# valores: list[int] = Lista de inteiros contidos em itens, mas sem valores repetidos
if __name__ == '__main__':
    itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    valores = []
    for i in itens:
        if i not in valores:
            valores.append(i)
    print(valores)
