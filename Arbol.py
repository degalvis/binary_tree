from Nodo import Nodo


class Arbol:
    def __init__(self, data):
        self.raiz = Nodo(data)
        
    def insertarRecursivo(self, nodo, data):
        
        if self.raiz == None:
            self.raiz = Nodo(data)
        else:
            if data > nodo.data:
                if nodo.der == None:
                    nodo.der = Nodo(data)
                else:
                    self.insertarRecursivo(nodo.der, data)
            elif data < nodo.data:
                if nodo.izq == None:
                    nodo.izq = Nodo(data)
                else:
                    self.insertarRecursivo(nodo.izq, data)
            else:
                return
    
    def insertar(self, data):
        self.insertarRecursivo(self.raiz, data)
        
        
    def imprimirRecursivo(self, nodo):
        if nodo != None:
            self.imprimirRecursivo(nodo.izq)
            print(nodo.data, end = ", ")
            self.imprimirRecursivo(nodo.der)
    
    def imprimir(self):
        self.imprimirRecursivo(self.raiz)