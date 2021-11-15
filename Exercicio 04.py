"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa
deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
comprar dividido pelo numero de meses a pagar. """
#entrada de dados
casavalor = int(input("Valor da casa: "))
salario = int(input("Salario: "))
anos = int(input("Quantidade de anos a pagar: "))
#processamento
meses = anos * 12
mensalidade = casavalor / meses
salario30 = (salario * 30) /100
#saida de dados
if(mensalidade > salario30):
  print("Financiamento recusado !")
else:
  print("A mensalidade será:600" + str(mensalidade))