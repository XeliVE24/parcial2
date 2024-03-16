import pandas as pd
from libs import *
inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

numero=int(input("Cual es mi numero?"))
archivo=input("Cual es el nombre del archivo a procesar?")

df=pd.read_excel(archivo)
print(df)

print("000000000000000000000000000000000000000000000000000000")
ArrayNum=df
###### numero en rojo 

#arbol simetrico 

NodoRaiz=nodo(0)

for i in range (1,len(ArrayNum),1):
    Agreganodos(NodoRaiz,ArrayNum[1])
Printarbol(NodoRaiz)

LVR(NodoRaiz,inOrderArr)
print("InOrder:")
print (inOrderArr)

VLR(NodoRaiz,PreOrderArr)
LRV(NodoRaiz,PostOrderArr)

print ("PreOrder:")
print(PreOrderArr)
print("PostOrder:")
print (PostOrderArr)
print("000000000000000000000000000000000000000000000000000000000000000000000000000000000")

#00000000000000000000000000000000000000000000000000000000000000000
print("nodo raiz :"+str(numero))
nodoRaiz=numero

for i in range (0,len(ArrayNum),1):
    if i == 0 :
        nodoRaiz = nodo (ArrayNum[i])
    else:
        nodoOrdenados(nodoRaiz,nodo(ArrayNum[i]))
        
pass
Printarbol(nodoRaiz)

print("recorrido de arbol ordenado:")