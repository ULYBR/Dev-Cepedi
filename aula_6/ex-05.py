# Exercício 5: Remover circunferências
# input:
# circunferencias: list[(float,float, raio)] = Lista de circunferências (xc, yc, raio)
# ponto: (float, float) = Ponto (x, y)
# output:
# circunferências que não foram atingidas pelo ponto

def remove_circunferencias(circunferencias, ponto):
    return [c for c in circunferencias if (ponto[0]-c[0])**2 + (ponto[1]-c[1])**2 > c[2]**2]
if __name__ == '__main__':
    circunferencias = [(0,0,1),
                       (1,1,1),
                       (2,2,1),
                       (3,3,1),
                       (4,4,1)]
    ponto = (1,2)
    print(remove_circunferencias(circunferencias, ponto))

