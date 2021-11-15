"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
quantidade de kWh consumida e o tipo de instalação: R para residencial, I para industrial e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir: 
● Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
● Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
● Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60. """

#entrada de dados
kWh = int(input("kWh consumida: "))
tipo = input("Tipo de instalação:\nR para residencial\nI para industrial\nC para comércios.\n")
#processamento

if(tipo == "R"):
  if(kWh < 500):
    value = kWh * 0.40
  else:
    value = kWh * 0.65
  print("R - Preço a pagar: " + str(value))
if(tipo == "I"):
  if(kWh < 1000):
    value = kWh * 0.55
  else:
    value = kWh * 0.60
  print("I - Preço a pagar: " + str(value))
if(tipo == "C"):
  if(kWh < 5000):
    value = kWh * 0.55
  else:
    value = kWh * 0.60
    #saida de dados
  print("C - Preço a pagar: " + str(value))

