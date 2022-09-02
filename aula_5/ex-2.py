if __name__ == "__main__":



    #criar um jogo da velha inteligente
    # 1. O jogo deve ser capaz de identificar se o jogador ganhou ou perdeu
    # 2. O jogo deve ser capaz de identificar se o jogo empatou
    # 3. O jogo deve ser capaz de identificar se o jogador pode ganhar na próxima jogada

    def mostrar_separador():
        print('-=-' * 15)


    def criar_tabuleiro():  # cria um tabuleiro vazio
        return list(range(1, 10))  # lista com os números entre 1 e 9


    def mostrar_tabuleiro(tabuleiro):
        print('  {}  |  {}  |  {}  '.format(*tabuleiro[:3]))  # mostra as 3 primeiras posições
        print('------+------+------')
        print('  {}  |  {}  |  {}  '.format(*tabuleiro[3:6]))  # mostra da quarta à sexta posição
        print('------+------+------')
        print('  {}  |  {}  |  {}  '.format(*tabuleiro[6:]))  # mostra as 3 últimas posições


    def pedir_jogada(tabuleiro, jogador):
        mostrar_separador()
        while True:
            try:  # não use isdigit(), capture o ValueError
                print(f'jogador atual: {jogador}')  # incluí esta mensagem para facilitar um pouco
                jogada = int(input('Digite uma posição no tabuleiro para jogar: '))
                if jogada <= 0 or jogada > len(tabuleiro):  # verifica se o valor não está fora dos limites do tabuleiro
                    print(f'Posição inválida: {jogada}')
                elif jogada in tabuleiro:
                    mostrar_separador()
                    return jogada  # retorna direto, não precisa do break
                else:
                    print('Você digitou um número já pedido, tente novamente')
            except ValueError:
                print('Você não digitou um número válido, tente novamente')


    def jogo_terminou(tabuleiro):
        posicoes_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]
        # verifica todas as combinações de posições vencedoras
        for pos1, pos2, pos3 in posicoes_vencedoras:
            if tabuleiro[pos1] == tabuleiro[pos2] == tabuleiro[pos3]:
                print(f'Temos um vencedor: {tabuleiro[pos1]}! Parabéns!')  # mudei a mensagem para mostrar quem ganhou
                # se já encontrei um vencedor, posso retornar direto (não precisa continuar verificando as outras combinações)
                return True

        # não tem vencedor, verifica se todas as posições estão ocupadas (não preciso mais do contador de jogadas)
        if all(posicao in ('X', 'O') for posicao in tabuleiro):
            print('Deu velha! Ninguém ganhou.')
            return True

        # jogo ainda não terminou
        return False


    import sys


    def verificar_jogar_novamente():  # mudei o nome "denovo" para algo mais significativo
        while True:  # use um loop em vez de chamar a função dentro dela mesma
            jogar_denovo = input('''
    Deseja jogar novamente?
    Digite S para SIM ou N para NÃO.
    ''').upper()  # já transforma em maiúscula aqui

            if jogar_denovo == 'S':
                mostrar_separador()
                break  # sai do while
            elif jogar_denovo == 'N':
                print('Até logo!')
                sys.exit()  # sai do programa
            else:  # incluí uma mensagem a mais para ajudar o usuário
                print('Você deve digitar "S" ou "N"')


    def dados_iniciais():  # o jogo começa com o jogador X e tabuleiro vazio
        print('Bem Vindo ao Jogo da Velha! Vamos começar!')
        return ('X', criar_tabuleiro())


    jogador, tabuleiro = dados_iniciais()
    while True:
        mostrar_tabuleiro(tabuleiro)

        # como o tabuleiro agora é uma lista, posso simplesmente marcar a jogada mudando-o diretamente
        # e ele substitui a lista_totalpalpites, que se torna redundante
        jogada = pedir_jogada(tabuleiro, jogador)
        tabuleiro[jogada - 1] = jogador
        jogador = 'O' if jogador == 'X' else 'X'  # troca o jogador de X para O ou vice-versa

        if jogo_terminou(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            verificar_jogar_novamente()
            # reinicio o tabuleiro
            jogador, tabuleiro = dados_iniciais()