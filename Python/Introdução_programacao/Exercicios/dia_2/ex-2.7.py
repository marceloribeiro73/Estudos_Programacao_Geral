# Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

# 	O número x é primo
# ou
# 	O número x não é primo

numero = int(input("Insira um numero: "))

if(numero % 2 == 0 and numero != 2 or numero == 0 or numero ==1 or numero == -1):
    print(f"O número {numero} não é primo")
else:
    print(f"O numero {numero} é primo")