import pandas as pd
from libs import *
df = pd.read_excel ("datos-Eval-2.xlsx")


inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

nodo1 =nodo(1)
nodo2=nodo(2)
nodo3= nodo(3)
nodo4= nodo(4)
nodo5= nodo(5)
nodo6= nodo(6)
nodo7= nodo(7)


linkhijo(nodo1,nodo2,nodo3)
linkhijo(nodo2,nodo4,nodo5)
linkhijo(nodo3,nodo6,nodo7)
print("Getarbol:")
print ( nodo1.getArbol())

print("--------------------------------------------------------------------------------------")

LVR(nodo1,inOrderArr)
print("InOrder:")
print (inOrderArr)



VLR(nodo1,PreOrderArr)
LRV(nodo1,PostOrderArr)


print ("PreOrder:")
print(PreOrderArr)
print("PostOrder:")
print (PostOrderArr)

print("-------------------------------------------------------------------------------")
arrNodos=[16,5,7,12,9,20,18,3,10,14]
nodoRaiz= None


for i in range (0,len(arrNodos),1):
    if i == 0 :
        nodoRaiz = nodo (arrNodos[i])
    else:
        nodoOrdenados(nodoRaiz,nodo(arrNodos[i]))
        
pass


Printarbol(nodoRaiz)