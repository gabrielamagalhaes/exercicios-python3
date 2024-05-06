largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura}, e sua área é de {area}m².')
print(f'Para pintar essa parede você precisará de {tinta:.2f}l de tinta.')


'''
Neste exercício:
    1 - Calcule a área da parede
    2 - Dada a área, calcule o quanto de tinta será necessário para pinta-la
        sabendo que a cada 2m² de parede você precisa de 1 litro de tinta para ser pintada
'''