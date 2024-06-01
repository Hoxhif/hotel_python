from .Habitacion import Habitacion
from .TipoHabitacion import TipoHabitacion
class Simple(Habitacion):
    def __init__(self, planta, puerta, precio):
        super().__init__(planta, puerta, precio)

    def get_numero_maximo_personas():
        tipo_habitacion = TipoHabitacion.SIMPLE
        return tipo_habitacion.value[1]
    
    def __str__(self):
        return f"{super().__str__()}, tipo Simple, máximo numero de personas: {self.get_numero_maximo_personas()}."