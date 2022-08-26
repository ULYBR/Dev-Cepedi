if __name__ == "__main__":

    texto = 'ulysses'
    termo = 'e'

    termo_encontrado = False
    for pos, _ in enumerate(texto):
        contador = 0
        for termo_pos, _ in enumerate(termo):
            letra_termo = termo[termo_pos]
            letra_texto = texto[pos + termo_pos]
            if letra_texto != letra_termo:
                break
            else:
                contador += 1

        if contador == len(termo):
           termo_encontrado = True
           print(f'O termo" {termo} "foi encontrado em {texto} na posição: {pos}')
           break



    if not termo_encontrado:
        print(f'O termo"{termo}" não foi encontrado :{texto}')


