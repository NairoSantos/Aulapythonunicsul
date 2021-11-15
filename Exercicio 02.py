""" Escreva um programa que calcular a categoria de um produto e determine o preço pela tabela: Categoria
1 valor de R$ 10,00; Categoria 2 valor de R$ 15,00; Categoria 3 valor de R$ 19,00; Categoria 4 valor de R$
23,00 e Categoria 5 valor de R$ 27,00. """
#entrada de dados
cat1 = "Categoria 1 valor de R$ 10,00"
cat2 = "Categoria 2 valor de R$ 15,00"
cat3 = "Categoria 3 valor de R$ 19,00"
cat4 = "Categoria 4 valor de R$ 23,00"
cat5 = "Categoria 5 valor de R$ 27,00"
#processamento
cat = int(input("Digite o numero da categoria do produtos. (1,2,3,4 ou 5)\n"))
if(cat == 1):
  print(cat1)
elif(cat == 2):
  print(cat2)
elif(cat == 3):
  print(cat3)
elif(cat == 4):
  print(cat4)
elif(cat == 5):
  print(cat5)
else:
  #saida de dados
  print("Categoria nao encontrada !")
