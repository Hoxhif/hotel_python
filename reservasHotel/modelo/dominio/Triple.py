from .Habitacion import Habitacion
from .TipoHabitacion import TipoHabitacion
class Triple(Habitacion):
    def __init__(self, planta, puerta, precio, num_camas_individuales, num_camas_dobles, num_banos):
        super().__init__(planta, puerta, precio)
        self.set_num_camas_individuales(num_camas_individuales)
        self.set_num_camas_dobles(num_camas_dobles)
        self.set_num_banos(num_banos)

    def get_numero_maximo_personas(self):
        tipo_habitacion = TipoHabitacion.TRIPLE.value[1]
        return tipo_habitacion
    
    def get_num_camas_individuales(self):
        return self.__num_camas_individuales
    
    def get_num_camas_dobles(self):
        return self.__num_camas_dobles
    
    def get_num_banos(self):
        return self.__num_banos
    
    def set_num_camas_individuales(self, num_camas_individuales):
        self.__num_camas_individuales = num_camas_individuales

    def set_num_camas_dobles(self, num_camas_dobles):
        self.__num_camas_dobles = num_camas_dobles
        self.__valida_num_camas()
    
    def __valida_num_camas(self):
        if not((self.get_numero_camas_individuales()==0 and self.get_numero_camas_dobles==1) or (self.get_numero_camas_individual()==2 and self.get_numero_camas_dobles==0)):
            raise ValueError("Las disposicion de una habitación doble solo puede ser 1 cama doble o 2 camas individuales.")
        
    def set_num_banos(self, num_banos):
        self.__num_banos=num_banos
        self.valida_num_banos()

    def valida_num_banos(self):
        if self.get_num_banos()<1 or self.get_num_banos>2:
            raise ValueError("Solo puede haber 1 o 2 baños en una habitación Triple.")

    def __str__(self):
        return f"{super().__str__()}, tipo Triple, máximo numero de personas: {self.get_numero_maximo_personas()}, número de canas individuales: {self.get_num_camas_individuales()}, número de canas dobles: {self.get_num_camas_dobles()}, número de baños: {self.get_num_banos()}."