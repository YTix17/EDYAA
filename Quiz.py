class Hotel:
    def __init__(self, num_habitaciones):
        self.num_habitaciones = num_habitaciones
        self.habitaciones_disponibles = list(range(1,num_habitaciones + 1))
        self.lista_huespedes = []
        
    def registrar_llegada(self, cedula, nombre, num_habitacion):
        if num_habitacion in self.habitaciones_disponibles:
            self.lista_huespedes.append({"cedula":cedula,"nombre":nombre,"habitacion":num_habitacion})
            self.habitaciones_disponibles.remove(num_habitacion)
        else:
            print(f"La habitación {num_habitacion} ya está ocupada.")
    
    def registrar_salida(self, cedula):
        for huesped in self.lista_huespedes:
            if huesped["cedula"] == cedula:
                self.habitaciones_disponibles.append(huesped["habitacion"])
                self.lista_huespedes.remove(huesped)
                return
            print(f"No se encontró al huésped con cédula {cedula}.")
    
    def consultar_huesped_por_cedula(self, cedula):
        for huesped in self.lista_huespedes:
            if huesped["cedula"] == cedula:
                return huesped
        return None
    
    def consultar_huespedes_por_orden_de_llegada(self):
        return self.lista_huespedes
    
    def consultar_habitaciones_disponibles(self):
        return self.habitaciones_disponibles
    
    def consultar_habitaciones_ocupadas(self):
        return [habitacion for habitacion in range(1,self.num_habitaciones + 1) if habitacion not in self.habitaciones_disponibles]

#Registro de personas
hotel = Hotel(5)
hotel.registrar_llegada("123","Pedro",2)
hotel.registrar_llegada("321","Carlos",4)
hotel.registrar_llegada("321","Luis",3)
#Muestra las habitaciones ocupada y disponibles como también los huéspedes
print("Habitaciones Disponibles:\n", hotel.consultar_habitaciones_disponibles())
print("Habitaciones Ocupadas:\n", hotel.consultar_habitaciones_ocupadas())
print("Consultar Huésped por Cédula:\n", hotel.consultar_huesped_por_cedula("123"))
print("Consultar Huéspedes por Orden de Llegada:\n", hotel.consultar_huespedes_por_orden_de_llegada())

#Formas y maneras de usar las demás funciones del programa solicitado
""" Para registrar la salida de un huésped, puedes usar:
hotel.registrar_salida(cedula)
# Para consultar información de un huésped por cédula, puedes usar:
hotel.consultar_huesped_por_cedula(cedula)
# Para consultar la lista de habitaciones disponibles, puedes usar:
hotel.consultar_habitaciones_disponibles()
# Para consultar la lista de habitaciones ocupadas, puedes usar 
hotel.consultar_habitaciones_ocupadas()"""
