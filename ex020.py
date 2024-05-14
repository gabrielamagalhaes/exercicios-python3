import random

nome_1 = str(input('Nome do primeiro aluno: '))
nome_2 = str(input('Nome do segundo aluno: '))
nome_3 = str(input('Nome do terceiro aluno: '))
nome_4 = str(input('Nome do quarto aluno: '))

lista = [nome_1, nome_2, nome_3, nome_4]
random.shuffle(lista)

print('A ordem de apresentação do trabalho será: ')
print(lista)