#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date #modulo utilizado para calculo do ano

print('Vamos descobrir como você está em relação ao alistamento militar.')
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano #Vai definir a idade atual

if idade == 18:
    print('Já chegou a hora de você se alistar ao serviço militar!')
    print('Não se esqueça, precisa se alistar esse ano!')
elif idade < 18:
    falta = 18 - idade
    print('Ainda não chegou a hora de você se alistar!')
    print('Você ainda deve aguardar {} anos para se alistar.'.format(falta))
else:
    passou = idade - 18
    print('Eita! Já passou da hora de você se alistar!!!')
    print('Você deveria ter se alistado a {} anos.'.format(passou))
