from .TipoHabitacion import TipoHabitacion
from .Habitacion import Habitacion
class Suite(Habitacion):

    def __init__(self, planta, puerta, precio, num_banos, jacuzzi):
        super().__init__(planta, puerta, precio)
        self.__set_num_banos(num_banos)
        self.__set_jacuzzi(jacuzzi)

    def get_numero_maximo_personas(self):
        tipo_habitacion = TipoHabitacion.SUITE.value[1]
        return tipo_habitacion

    def set_num_banos(self, num_banos):
        self.__num_banos=num_banos
        self.valida_num_banos()

    def get_num_banos(self):
        return self.__num_banos

    def is_tiene_jacuzzi(self):
        return self.__jacuzzi
    
    def set_jacuzzi(self, jacuzzi):
        if isinstance(jacuzzi, bool):
            return jacuzzi
    
    def valida_num_banos(self):
        if self.get_num_banos()<1 or self.get_num_banos>2:
            raise ValueError("Solo puede haber 1 o 2 baños en una habitación Triple.")
        
    def __str__(self):
        if self.is_tiene_jacuzzi():
            cadena = "Con Jacuzzi"
        else: cadena = "Sin Jacuzzi"
        return f"{super().__str__()}, tipo Suite, máximo numero de personas: {self.get_numero_maximo_personas()}, número de baños: {self.get_num_banos()}, {cadena}."