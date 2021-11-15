""" Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você
deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação
solicitada."""
#entrada de dados
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
ope = int(input("Selecione a operação:\n1.soma\n2.subtração\n3.multiplicação\n4.divisão\n"))
#processamento
if(ope == 1):
  print("A soma é " + str(a+b))
elif(ope == 2):
  print("A subtração é " + str(a-b))
elif(ope == 3):
  print("A multiplicação é " + str(a*b))
elif(ope == 4):
  print("A divisão é " + str(a/b))
else:
  #saida de dados
  print("Operação inválida")