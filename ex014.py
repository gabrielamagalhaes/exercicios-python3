temp_celcius = float(input('Informe a temperatura em °C: '))

temp_farenheit = temp_celcius * 1.8 + 32

print('A temperatura de {:.1f}°C, corresponde a {:.1f}°F'.format(temp_celcius, temp_farenheit))


'''
Neste exercício:
    1 - Faça o calculo de conversão de temperaturas de Celcius para Farenheint.


    * Outro modo de realizar o calculo:
        - Utilizando outra fórmula de calculo da conversão:
            temp_farenheit = ((9 * temp_celcius) / 5) + 32
'''