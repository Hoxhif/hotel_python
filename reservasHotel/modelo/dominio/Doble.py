from .Habitacion import Habitacion
from .TipoHabitacion import TipoHabitacion
class Doble(Habitacion):

    def __init__(self, planta, puerta, precio, num_camas_individuales, num_camas_dobles):
        super().__init__(planta, puerta, precio)
        self.__set_numero_camas_individuales(num_camas_individuales)
        self.__set_numero_camas_dobles(num_camas_dobles)
    
    def get_numero_maximo_personas():
        tipo_habitacion = TipoHabitacion.DOBLE
        return tipo_habitacion.value[1]

    def get_numero_camas_individuales(self):
        return self.__camas_individuales
    
    def get_numero_camas_dobles(self):
        return self.__camas_dobles

    def __valida_num_camas(self):
        if not((self.get_numero_camas_individuales()==0 and self.get_numero_camas_dobles==1) or (self.get_numero_camas_individual()==2 and self.get_numero_camas_dobles==0)):
            raise ValueError("Las disposicion de una habitación doble solo puede ser 1 cama doble o 2 camas individuales.")
        
    def __set_numero_camas_individuales(self, num_camas_individuales):
        self.__set_numero_camas_individuales = num_camas_individuales

    def __set_numero_camas_dobles(self, num_camas_dobles):
        self.__set_numero_camas_dobles=num_camas_dobles
        self.__valida_num_camas()

    def __str__(self):
        return f"{super().__str__()}, tipo Doble, máximo numero de personas: {self.get_numero_maximo_personas()}, número de camas individuales: {self.get_numero_camas_individuales()}, número de camas dobles: {self.get_numero_camas_dobles()}."