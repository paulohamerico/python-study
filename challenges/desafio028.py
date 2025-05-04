#Escreva um programa que faça o computaodr "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
ni = randint(0, 5) #Faz o computador escolher um numero entre 0 e 5
print('-=-' * 22)
print('Pensei em um número entre 0 e 5, será que você adivinha qual foi?')
print('-=-' * 22)
ne = int(input('Qual você acha que foi o número? '))
print('Hmmmm... deixa eu ver....')
sleep(1.3) #Adiciona uma pausa dramatica para o "jogo"
if ne == ni:
    print('PARABÉNS, VOCÊ ACERTOU! O número escolhido era {}, você está bom de palpite em!'.format(ni))
else:
    print('GANHEI! HAHAHAHA O número escolhido era {}, você perdeu... Tente novamente!'.format(ni))
print('FIM')
