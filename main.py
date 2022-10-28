from Arbol import Arbol

def main():
    f = open("archivo.txt", "r")

    encabezador = Arbol("Indice libro")

    with f as file:
        for line in file:
            encabezador.insert(line)
            

