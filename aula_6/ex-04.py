# Exercício 4: busca binária
# # input:
# # itens: list[int] - Lista de inteiros
# # elemento: int - Termo de busca
# # output:
# # (indice se itens[indice] == elemento; senão None, numero_comparacoes)
# # Lançar uma exceção, caso a lista não seja ordenada

def busca_binaria (array, elemento, inicio=0, fim=None):
    if fim is None:
        fim = len(array)-1


    if inicio <= fim:
        meio = (inicio + fim) // 2
        if array[meio] == elemento:
            return meio
        if   elemento < array[meio]:
            return busca_binaria(array, elemento, inicio, meio-1)
        else:
            return busca_binaria(array, elemento, meio+1, fim)
    return None

if __name__ == '__main__':
    lista = [1, 5, 2, 8, 55, 100]
    lista.sort()
    print(lista)
    print(busca_binaria(lista, 8))



