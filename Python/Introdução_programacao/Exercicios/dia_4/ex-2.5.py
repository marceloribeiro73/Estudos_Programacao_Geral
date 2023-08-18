# Escreva um programa que crie um dicionário com nomes de frutas 
# como chaves e seus respectivos preços como valores. 
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

#Maçã: R$1,50     Banana: R$2,75       Uva: R$1,90      Pera: R$1,25  
#Laranja: R$0,65     Limão: R$1,25       Goiaba: R$2,15      Abacaxi: R$3,20     Jaca: R$5,80        


def load_fruits_dict():
    """
    Função que carrega o dicionario com as frutas e os seus valores 
    """
    fruits = {
            "Maçã":1.50,
            "Laranja":0.65,
            "Banana": 2.75,
            "Limão": 1.25,
            "Uva":1.90,
            "Goiaba":2.15,
            "Pera":1.25,
            "Abacaxi":3.20,
            "Jaca":5.80  
            }
    return fruits


fruta_busca = input("Qual fruta você quer saber o preço: ")

frutas = load_fruits_dict()

fruta_preco = frutas.get(fruta_busca)

if fruta_preco != None:
    print(f"O preço da fruta {fruta_busca} é R${fruta_preco:.2f}")
else:
    print(f"A fruta {fruta_busca} não esta cadastrada")