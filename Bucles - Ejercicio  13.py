palabra = input("Ingrese una palabra de mas de 4 letras para ver el eco, o salir para terminar:")
cantidad = len(palabra)
i = 0
while palabra != "salir":
		while i < 3:
			print((palabra[-3]),(palabra[-2]),(palabra[-1]))
			i = i + 1
if palabra == "salir":
	exit()
