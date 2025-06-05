#Refaça o desafio 009, mostrando a tabuado d eum número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o número da tabuada que quer consultar: '))
print('-='*7)
print(f'Tábuada do {n}:')
print('-='*7)
for c in range(1, 11):
    print(f'{n:2} x {c:2} = {c*n:3}')
print('-='*7)