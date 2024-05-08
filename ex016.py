from math import trunc

numero = float(input('Digite um valor: '))
numero_int = trunc(numero)

print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, numero_int))

'''
        - Usando módulos
    Neste esxercício:
    1 - Transformar o valor dado em um número inteiro usando a biblioteca Math

    *Outro modo de fazer o exercício:
        - Sem importar biblioteca, usando uma função built-in do python:
            numero = float(input('Digite um valor: '))
            numero_int = int(numero)

            print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, numero_int))

'''