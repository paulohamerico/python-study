#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

s = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º numero: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos números pares é {s}.')
