

from re import I


class Nodo:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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
       
# Print the Tree
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

f = open("archivo.txt", "r")

#árbol term
terminos = []
for x in f:
    if (x[0]=="m"):
     word = x[1:8]
     terminos.append(word)
     
cabezat = Nodo((terminos[0])[1:8])
for i in range(1, len(terminos)):
    cabezat.insert(str(i))

print(cabezat.inorderTraversal(cabezat))
print(terminos)

