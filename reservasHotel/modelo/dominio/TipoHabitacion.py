from enum import Enum
class TipoHabitacion(Enum):
    # Cadena_A_Mostrar | Num_Max_Personas
    SIMPLE = "Simple", 1
    DOBLE = "Doble", 2
    TRIPLE = "Triple",3 
    SUITE = "Suite", 4

    def __str__(self):
        return self.value[0]

