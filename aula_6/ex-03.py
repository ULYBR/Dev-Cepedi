# Exercício 3: busca linear
# input:
# itens: list[int] - Lista de inteiros
# elemento: int - Termo de busca
# output:
# (indice se itens[indice] == elemento; senão None, numero_comparacoes)

def busca_linear (lista, elemento):
    numero_comparacoes = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

if __name__ == '__main__':
    list = [1, '2',"python",8, 55, 10]
    elemento = input("Digite o elemento a ser buscado: ")
    if busca_linear(list, elemento) is None:
        print('Elemento não encontrado')
    print(busca_linear(list, elemento))
