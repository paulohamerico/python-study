#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
letras = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format((nome.upper())))
print('Seu nome em minúsculas é: {}'.format((nome.lower())))
print('Ao todo seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome é {} e tem {} letras.'.format(letras[0], len(letras[0])))
