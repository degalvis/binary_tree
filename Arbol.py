from Nodo import Nodo 

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Nodo(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                        self.right = Nodo(data)
                else:
                        self.right.insert(data)
        else:
            self.data = data
