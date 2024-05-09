from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(ca, co)

print(f'A hipotenusa vai medir {hip:.2f}')


'''
    Neste exercício:
    1 - Calcular o valor da hipotenusa do triângulo.
        -> Estou importando a biblioteca 'Math' e utilizando a função 'hypot()' que faz o calculo da hipotenusa.

    *Outro modo de fazer o exercício:
        - Reescrevendo a fórmula de calculo das seguintes formas: 
            soma_catetos = (co ** 2 + ca ** 2) * (1/2) 

            soma_catetos = co ** 2 + ca ** 2
            hip = math.sqrt(soma_catetos)
'''