#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
import time

print('Vamos jogar Jokenpô!')
print('Escolha uma das opções abaixo:')
print('1 = Pedra')
print('2 = Papel')
print('3 - Tesoura')

opcoes = ['Pedra', 'Papel', 'Tesoura']
usuario = int(input('Qual sua escolha?: '))
computador = randint(1,3)

if 1 <= usuario <= 3:
    print('JO...')
    time.sleep(0.5)
    print('KEN...')
    time.sleep(0.5)
    print('PÔ!')

    print(f'Você escolheu: {opcoes[usuario - 1]}')
    print(f'O computador escolheu: {opcoes[computador - 1]}')

    if usuario == computador:
        print('Empate!')
    elif (usuario == 1 and computador == 3) or (usuario == 2 and computador == 1) or (usuario == 3 and computador == 2):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
else:
    print('Opção inválida! Escolhe apenas entre 1, 2 e 3.')