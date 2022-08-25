if __name__ == '__main__':
    #crie um programa que converte segundos em hh:mm:ss

    #seg=int(input('digite em segundos : '))
    #min=seg//60
    #horas=min//60

 #print(f'horas:{horas}minutos:{min}segundos:{seg}')

#resolução

  tempo=int(input('segundos: '))
  segundos = tempo

  horas = segundos // (60*60)

  minutos = segundos // 60

  segundos %= 60

print(f' {tempo}s equivale a {horas:02d}:{minutos:02d}:{segundos:02d}')