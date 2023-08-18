# Faça um programa que receba o nome e a idade de uma pessoa. 
# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
# 	“Fulano, você não pode dirigir nem beber”
# Para as pessoas entre 18 e 65 anos, exiba o aviso:
# 	“Fulano, bebida liberada! Só não vale dirigir!”
# Para as pessoas com mais de 65 anos, exiba o aviso:
# 	“Fulano, beba com muita moderação!”

nome = input("Entre com o seu nome: ")
idade = int(input("Entre com a sua idade"))

if idade < 18:
    print(nome, ", voce não pode dirigir nem beber", sep="")
elif idade > 65:
    print(nome, "beba com muita moderação!")    
else:
    print(nome, ", bebida liberada! Só não vale dirigir!", sep="")