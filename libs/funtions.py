from .classes import *
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

