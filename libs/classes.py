class nodo ():
    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None 
        pass

    def __str__(self):
        return f"Valor:{self.valor} ,izq:{self.izq} ,der:{self.der}"


    def getArbol(self):
        strOut =""
        strOut += f" NP {(self.valor)}"
        
        if type(self.izq) != type (None):
            strOut += f" iz[{self.valor}]-> [{self.izq}]"
        
        if self.der is not None :
            strOut +=f" der[{self.valor}-> [{self.der}]]"
        return strOut

    def __str__ (self):
        return f"{self.valor}"
    

    