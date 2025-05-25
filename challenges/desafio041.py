#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento d eum atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: Sênior
#Acima: Master

from datetime import date

print('Vamos categorizar o participante.')
ano = int(input('Digite o ano de nascimento do participante: '))
idade = date.today().year - ano
print('O participante tem {} anos.'.format(idade))

if idade <= 9:
    print('Por isso ele está na categoria "Mirim".')
elif idade <= 14:
    print('Por isso ele está na categoria "Infantil".')
elif idade <= 19:
    print('Por isso ele está na categoria "Junior".')
elif idade <= 25:
    print('Por isso ele está na categoria "Sênior".')
else:
    print('Por isso ele está na categoria "Master".')
