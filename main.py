# Restrictions:
#     1. First element of txt file gotta be a term
#     2. Second elemento txt file gotta be a subterm
#     3. Sub/term can only apear in 9 pages
#     4. if appear iin a page of one digit always put a zerobefore the number, example: 09,01

from Arbol import Arbol
import re

f = open("Archivo.txt")
words = f.readlines()

allesWords = []

for n in words:
    regexA = re.split('(\d+)', n)
    allesWords.append((regexA[0])[1:])
    

if (words[0])[0:1] == "m":
    treeM = Arbol(allesWords[0])
    
counter = 0
alles = []

print(allesWords)

for line in words: #
    if line[0:1] == "n" or line[0:1] == "s": #If word stars with n o s put number in alles[]
        regex = re.split('(\d+)', line)#list: separated words and numbers
        alles.append(regex[1])
        

for i in range(len(allesWords)):
    w = words[i]
    
    if w[0:1] == "m":
        treeM.insertar(allesWords[i]) #Insert term m in main tree 
        wP = allesWords[i+1] #Next word after M term
        treeN = Arbol(wP) 
        treeM.raiz.subT = treeN  
        j = i+2
        wP = words[j]
        
        treeP = Arbol(alles[counter])
        treeN.raiz.pages = treeP

        while (wP[0:1] == "n" or wP[0:1] == "s"):
            counter+=1
            subTRegex = re.split('(\d+)', wP)
            wP = (subTRegex[0])[1:]
            treeN.insertar(wP)
            treeP.insertar(alles[counter])
            j+=1
            
            if j < len(words):
                wP = words[j]
            else:
                break
            
        #Go through all the tree and check the one that has .subT == None
        #Insert treeN to that
        treeM.insertarSubT(treeN)
        #treeN.insertarPages(treeP)
        
# treeM.imprimir()

treeM.imprimir()
#print("\n")
#treeN.imprimir()

#treeP.raiz.izq.pages.imprimir()