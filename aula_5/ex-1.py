if __name__ == "__main__":
#criar um menu que permita ao usuario escolher entre as opcoes de 1 a 5 sendo ele:
# 1 Inserir inserir um grupo de trabalho em uma lista,2. Editar um grupo de trabalho,
#3. Consultar um grupo de trabalho,4. Remover um grupo de trabalho em uma lista
#5. Salvar de uma lista para um JSON os grupos de trabalho e sair do programa que cria um arquivo JSON
# com os grupos de trabalho
    import json
    def menu():
        print('1 - Inserir')
        print('2 - Editar')
        print('3 - Consultar')
        print('4 - Remover')
        print('5 - Salvar')
        print('6 - Sair')
        opcao = int(input('Escolha uma opção: '))
        return opcao
    def inserir():
        grupo = input('Digite o nome do grupo: ')
        lista.append(grupo)
        print('Grupo inserido com sucesso!')
    def editar():
        grupo = input('Digite o nome do grupo: ')
        if grupo in lista:
            novo_grupo = input('Digite o novo nome do grupo: ')
            lista[lista.index(grupo)] = novo_grupo
            print('Grupo editado com sucesso!')
        else:
            print('Grupo não encontrado!')
    def consultar():
        grupo = input('Digite o nome do grupo: ')
        if grupo in lista:
            print('Grupo encontrado!')
        else:
            print('Grupo não encontrado!')
    def remover():
        grupo = input('Digite o nome do grupo: ')
        if grupo in lista:
            lista.remove(grupo)
            print('Grupo removido com sucesso!')
        else:
            print('Grupo não encontrado!')
    def salvar():
        with open('grupos.json', 'w',encoding = "utf - 8") as arquivo:
            json.dump(lista, arquivo)
            print('Grupos salvos com sucesso!')
    lista = []
    while True:
        opcao = menu()
        if opcao == 1:
            inserir()
        elif opcao == 2:
            editar()
        elif opcao == 3:
            consultar()
        elif opcao == 4:
            remover()
        elif opcao == 5:
            salvar()
        elif opcao == 6:
            break
        else:
            print('Opção inválida!')


