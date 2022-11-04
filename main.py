from Arbol import Arbol
import re

f = open("Archivo.txt")
words = f.readlines()

if (words[0])[0:1] == "m":
    treeM = Arbol(words[0])

for i in range(len(words)):
    w = words[i]
    
    if w[0:1] == "m":
        treeM.insertar(words[i])
        wP = words[i+1] #Second input gotta be always a subterm
        treeN = Arbol(wP)
        treeM.raiz.pages = treeN
        j = i+2
        wP = words[j]
        
        while (wP[0:1] == "n" or wP[0:1] == "s"):
            treeN.insertar(wP)
            j+=1
            
            if j < len(words):
                wP = words[j]
            else:
                break

                
# for line in f:
#     word = f.readline()
    
#     if word[0:1] == "m":
#         wordSplit = re.split(r'(\d+)', word)
#         root.insertar(wordSplit)

treeM.imprimir()
treeM.raiz.der.pages.imprimir()