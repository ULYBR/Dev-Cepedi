# Exercício 1: N é primo?
# input:
# N: int - Número natural não nulo
# output:
# True, se N for divisível apenas por 1 e ele mesmo; senão False
if __name__ == '__main__':
    def primo (n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for x in range(2, n):
                if n % x == 0:
                    return False
            return True

    print(primo(1))


