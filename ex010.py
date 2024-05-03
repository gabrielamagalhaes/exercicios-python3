real = float(input('Quanto dinheiro você tem na carteira? '))

print(f'Com R${real}, você pode comprar US${real / 5.07 :.2f}.')


''' - Usando o .format()

print('Com R${}, você pode comprar US${:.2f}.'.format(real, (real / 5.07)))
'''
