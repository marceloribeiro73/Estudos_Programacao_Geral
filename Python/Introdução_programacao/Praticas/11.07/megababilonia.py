import random as rd
numeros_entrada =[]
numeros_gerados =[]
i =0
for i in range(6):
    numero= int(input(f'Insira o {i+1}º numero entre 01 e 60: '))
    while (numero < 1 or numero > 60) or numeros_entrada.count(numero) > 0:
        if numeros_entrada.count(numero) > 0:
            print(f'\nNumero já foi inserido, por favor insira outro numero')
        numero= int(input(f'\nInsira o {i+1}º numero entre 01 e 60: '))
    else:
        numeros_entrada.append(numero)
#Carregando a lista 
i = 0 
for i in range(6):
    numero = rd.randrange(1,60)
    while (numero < 1 or numero > 60) or numeros_gerados.count(numero) > 0 :
        numero = rd.randrange(1,60)
    else:
        numeros_gerados.append(numero)

print(numeros_entrada)
print(numeros_gerados)
numeros_acertos = []
i=0
for i in range(6):
    numero_entrada = numeros_entrada[i]
    if numeros_gerados.count(numero_entrada) > 0:
        numeros_acertos.append(numero_entrada)

if len(numeros_acertos) > 0:
    print(f"Parabens, voce acertou as {len(numeros_acertos)} dezenas: ")
    print(f'Numeros acertados: {numeros_acertos}')
    print(f'Numeros sorteados: {numeros_gerados}')
else:
    print("Voce não acertou nenhuma dezena")
    print(f"Numeros sorteados {numeros_gerados}")
