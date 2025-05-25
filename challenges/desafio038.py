#Escreva um programa que leia dois números inteiros e compare-os, montrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maios, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('O primeiro número é {} e o segundo número é {}'.format(n1, n2))
if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif n1 < n2:
    print('O segundo número é maior.')
else:
    print('O primeiro númerio é maior.')
