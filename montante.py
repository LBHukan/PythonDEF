p = float(input("Digite o Capital: "))
i = float(input ("Digite a taxa de Juros: "))
n = float(input("Digite o numero de periodos: "))
pe = i / 100

j = p * pe * n
m = p + j

trunch1 = str(j).split('.')
trunch2 = str(m).split('.')

print("Valor do Juros: " + str(trunch1[0]))
print("Decimais Juros: " + str(trunch1[1]))
print("Valor Montante: " + str(trunch2[0]))
print("Decimais Montante: " + str(trunch2[1]))