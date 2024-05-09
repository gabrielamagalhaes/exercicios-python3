import math

ang = float(input('Digite o ângulo que você deseja: '))

#apesar de existir a função que calcula sen, cos e tg, o valor passado em 'X' não está em graus mas sim em radiando
#portanto devemos converter o valor recebido em radiando, para depois calcular o sen, cos ou tg
seno = math.sin(math.radians(ang))
print(f'O ângulo de {ang} tem o Seno de {seno:.2f}')

cosseno = math.cos(math.radians(ang))
print(f'O ângulo de {ang} tem o Cosseno de {cosseno:.2f}')

tangente = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem a Tangente de {tangente:.2f}')

