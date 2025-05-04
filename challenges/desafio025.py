#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite o nome completo da pessoa: ')).strip()
verifica = 'SILVA' in nome.upper()
print('O nome {} tem "Silva"?\n{}.'.format(nome, verifica))
