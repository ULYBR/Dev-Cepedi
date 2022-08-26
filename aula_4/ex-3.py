#faça um programa que  Confere parênteses.
if __name__ == "__main__":
    aberto = fechado = 1
    expr = str(input('digite uma expressão com 0 ou mais  parênteses: '))

    if expr == '(':
        aberto += 1
    elif expr == ')':
        fechado += 1

    if aberto == fechado :
        if "(" in expr and ")" in expr:
            print(f'o texto digitado {expr} tem  parentêses')




        else :
            print(f'o texto digitado {expr} não parentêses')

    else:
        print("valor inválido!")
