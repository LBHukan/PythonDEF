from random import randint

def rand_p_i():
	ran = randint(0, 100)
	sobra = ran % 2
	if sobra == 0:
		return True
	elif sobra == 1:
		return False

while True:
	
	while True:
		escolha = rand_p_i()
		variavel = bool()
		numero = int(input("1 para Impar e 2 para Par"))
		if numero == 1:
			variavel = False
		elif numero == 2:
			variavel = True
		print (escolha)
		break
	while True:
		if (escolha == True) and (escolha == variavel):
			print ("par")
		elif (escolha == False) and (escolha != variavel):
			print("impar")
		print(escolha)
		print(variavel)
		break