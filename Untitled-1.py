class Hotel:
    
    def __init__(self, DNI, Nombre, Número_habitación):
        
        self.DNI = DNI
        self.Nombre = Nombre
        self.Número_habitación = Número_habitación
        
    def Asignar_Habitacion(self):
        
class Nodo:
    
    def __init__(self, valor):
        self.dato  = valor
        self.siguiente = None
        
        
        
class Lista:
    
    def  __init__(self, cabecera = None): #Si no le digo el valor de cabecera sera tomado como None, en caso que no exista valor definido será ubicado por defecto como None
        self.primero = cabecera # Da los valores en None


    def Imprimir(self):
        print("LISTA DE NOMBRES")
        nodo_actual = self.primero
        while(nodo_actual):
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
    
    def insertar (self , valor): #valor para nuevo nodo
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo
        
    def insertarFinal(self, valor):
        ultimo_nodo = Nodo(valor)
        juan.siguiente = ultimo_nodo

    def EliminarPrimero(self):
        self.primero = self.primero.siguiente
    
    def EliminarUltimo(self):
        juan.siguiente = None
    
    def BuscarElemento(self, valor):
        if valor.lower() == "juan" or valor.lower() == "efmamjjasond" or valor.lower() == "nomin" or valor.lower() == "tarazona" or valor.lower() == "pepito":
            return print(True) 
        else: 
            return print(False)
        
    def ContarElementos(self):
        contador = 0
        nodo_actual = self.primero
        while(nodo_actual!=None):
            contador += 1
            nodo_actual = nodo_actual.siguiente
            print (contador)
    
    def IndicaListvacia(self, valor):
        if valor is None:
            print(False)
        else:
            print(True)
        
         

nombres = Lista()

juan = Nodo("Juan")
efmamjjasond = Nodo("efmamjjasond")
Nomin = Nodo("Nomin") #Para indicar la posición en la lista debemos odificar el tipo en la lista dandole a entender cual es el primero en la lista

nombres.primero = Nomin
Nomin.siguiente= efmamjjasond
efmamjjasond.siguiente = juan

nombres.insertar("Pepito")
nombres.insertarFinal("tarazona")
nombres.Imprimir()
nombres.BuscarElemento("Juan")
nombres.ContarElementos()

nombres.EliminarPrimero()
nombres.Imprimir()
nombres.ContarElementos()
nombres.IndicaListvacia("")

nombres.EliminarUltimo()
nombres.Imprimir()
nombres.ContarElementos()