#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

print('Vamos calcular a situação do aluno!')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A média foi {:.1f}.'.format(media))
if media < 5.0:
    print('O aluno está REPROVADO!')
elif media >= 7.0:
    print('O aluno está APROVADO!')
else:
    print('O aluno está de RECUPERAÇÃO!')
