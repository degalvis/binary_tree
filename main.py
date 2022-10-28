from Arbol import Arbol
    
f = open("Archivo.txt")

encabezador = Arbol("Indice libro")


for line in f:
    encabezador.insert(line)
    

print("Hola Mundo")

print(encabezador)

        