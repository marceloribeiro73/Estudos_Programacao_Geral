# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 0, 1, 1, 2, 3, 5,...

# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y


numero_imput = int(input("Insira um numero: "))

numero_n0 =0
numero_n1 = 1
numero_n =1

i = 0
for i in range (i, numero_imput+1):
    if(i == numero_imput):
        print(f"A posição {i} corresponde ao numero {numero_n}")
    numero_n0 = numero_n1
    numero_n1 = numero_n
    numero_n = numero_n0+numero_n1