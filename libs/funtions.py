from .classes import *
import openpyxl
import pandas as pd




def marcarNum(archivo, numero):
    # Cargar el archivo Excel
    wb = openpyxl.load_workbook(archivo)
    sheet = wb.active

    # Leer el contenido del archivo Excel y convertirlo a un DataFrame de pandas
    data = sheet.values
    df = pd.DataFrame(data, columns=[col[0].value for col in sheet.iter_cols()])

    print("\033[34m Contenido del archivo Excel:\033[0m")
    
    for index, row in df.iterrows():
        for col_name, cell_value in row.items():
            if cell_value == numero:
                df.loc[index, col_name] = f"\033[91m{numero}\033[0m"

    print(df)



def linkhijo (nodoPadre, nodoHijoiz=None , nodoHijoDer=None):
    if nodoHijoiz is not None :
        nodoPadre.izq =nodoHijoiz
    if nodoHijoDer is not None:
        nodoPadre.der=nodoHijoDer
    pass

#arbol simetrico 
def LVR (nodo,inOrderArr):

    if nodo is not None:
        nodoPadre=nodo
        LVR(nodoPadre.izq,inOrderArr)
        inOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.der,inOrderArr)

    return inOrderArr 


    
def VLR(nodo,PreOrderArr):
  
    if nodo is not None:
        nodoPadre=nodo
        PreOrderArr.append(nodoPadre.valor)
        VLR(nodoPadre.izq,PreOrderArr)
        VLR(nodoPadre.der,PreOrderArr)

    return PreOrderArr 
    
    
def LRV(nodo,PostOrderArr):
  
    if nodo is not None:
        nodoPadre=nodo
        LRV(nodoPadre.izq,PostOrderArr)
        LRV(nodoPadre.der,PostOrderArr)

        PostOrderArr.append(nodoPadre.valor)
       
    return PostOrderArr 


#-------------inicio-----------
def nodoOrdenados(nodoPadre,newNodo):
    if newNodo.valor < nodoPadre.valor :#izquierda 
        nodoHijo=nodoPadre.izq
        if nodoPadre.izq is None:
            nodoPadre.izq = newNodo

        else:
            nodoOrdenados(nodoHijo,newNodo)
           
    if newNodo.valor> nodoPadre.valor :#derecha
        nodoHijo=nodoPadre.der
        if nodoPadre.der is None:
            nodoPadre.der= newNodo
        else:
            nodoOrdenados(nodoHijo,newNodo)
            
    pass
#------------fin---------------


def Printarbol(nodo):

    if nodo is not None:
        nodoPadre=nodo
        print(nodoPadre.getArbol())
        Printarbol(nodoPadre.izq)
        Printarbol(nodoPadre.der)

    return 0


def Agreganodos (currentNodo,nuevoNum):
    cola=[]
    cola.append(currentNodo)

    while cola:
        currentNodo = cola.pop(0)

        if currentNodo.izq is None:
            currentNodo.izq= nodo(nuevoNum)
            return 0
        if currentNodo.der is None:
            currentNodo.der = nodo (nuevoNum)
            return 0 
        
        cola.append(currentNodo.izq)
        cola.append(currentNodo.der)
        
    return 0 

