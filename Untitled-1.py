class Hotel:
    
    def __init__(self,):
        self.Número_habitación = [ 'A' , 'B', 'C', 'D']
        
class Huesped(Hotel):
    
    def __init__(self, DNI, Nombre):
        self.DNI = DNI
        self.Nombre = Nombre 
    
    def  Asignar_Habitacion(self, Habitación_seleccionada):
        
        Asignar_habitación = []   