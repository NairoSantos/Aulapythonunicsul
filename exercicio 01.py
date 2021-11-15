'''
01 – Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 
para viagens mais longas. 
'''

#entrada de dados
percorrer = float(input("Qual distância(km) prentende percorrer para calculo do valor da passagem: "))

#processamento

if percorrer <= 200:
    valor = percorrer * 0.50
else:
    percorrer > 200
    valor= percorrer * 0.45


#saida de dados

print("Valor da passagem a pagar pela distancia é: R$%4.2f" %valor)