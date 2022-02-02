frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra a buscar: ")
cuenta = 0
for i in range(len(frase)):
	if letra == frase[i]:
		cuenta = cuenta + 1
print(cuenta)