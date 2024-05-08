dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi rodado? '))

dias_alugado = dias * 60
km_rodado = km * 0.15

total_aluguel = dias_alugado + km_rodado

print('O total a pagar é de R${:.2f}'.format(total_aluguel))


'''
Neste exercício:
    1 - Calcule o quanto deve-se pagar pelo aluguel do carro, sabendo que:
        - Cada km rodado = R$0,15
        - Cada dia rodado = R$60,00
'''