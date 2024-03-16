
import pandas as pd
from libs import *
inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

numero=int(input("Cual es mi numero?"))
archivo=input("Cual es el nombre del archivo a procesar?")

df=pd.read_excel(archivo)
marcarNum(archivo,numero)


print("----------------------------------------------------------")
print("\033[34m arbol binario simetrico:\033[0m")
ArrayNum=df.values.flatten().tolist()

#arbol simetrico 

NodoRaiz=nodo(ArrayNum[0])

for i in range (1,len(ArrayNum),1):
    Agreganodos(NodoRaiz,ArrayNum[i])
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
print("-----------------------------------------------------------")

#00000000000000000000000000000000000000000000000000000000000000000
print("\033[34m arbol ordenado :\033[0m")
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

LVR(nodoRaiz,inOrderArr)
print("Recorrido del arbol ordenado:")
print(inOrderArr)