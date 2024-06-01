from enum import Enum
class Regimen(Enum):
                # Cadena_A_Mostrar | Incremento_Precio
    SOLO_DESAYUNO = ("Solo Desayuno", 0.0) 
    ALOJAMIENTO_DESAYUNO = "Alojamiento y Desayuno", 15.0
    MEDIA_PENSION = "Media Pensión", 30.0
    PENSION_COMPLETA = "Pensión Completa", 50.0
    
    def __str__(self):
        return self.value[0]

