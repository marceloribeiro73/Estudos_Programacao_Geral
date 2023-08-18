# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

# 	O número x é impar
# ou
# 	O número x é par

numero = int(input("Insira um numero inteiro"))

if (numero % 2  != 0):
    print(f"O número {numero} é impar")
else:
    print(f"O número {numero} é par")