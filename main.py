
import pandas as pd
from libs import *
inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]
print("\033[34m Xeli Vargas n:33 \033[0m")
numero=int(input("Cual es mi numero?"))
archivo=input("Cual es el nombre del archivo a procesar?")

df=pd.read_excel(archivo)
marcarNum(archivo,numero)


print("----------------------------------------------------------")
print("\033[34m arbol binario simetrico:\033[0m")
ArrayNum=df.values.flatten().tolist()

#arbol simetrico 

NodoRaiz=nodo(ArrayNum[0])

for i in range (0,len(ArrayNum),1):
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
nodoRaiz = nodo(numero)
for i in range (1,len(ArrayNum),1):
        nodoOrdenados(nodoRaiz,nodo(ArrayNum[i-1]))
Printarbol(nodoRaiz)






LVR(nodoRaiz,inOrderArr)
print("Recorrido del arbol ordenado:")
print(inOrderArr)