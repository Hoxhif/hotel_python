from vista.Vista import Vista
from modelo.Modelo import Modelo
from controlador.Controlador import Controlador
class MainApp:
 
    if __name__ == "__main__":
            modelo = Modelo()
            vista = Vista()
            controlador = Controlador(modelo, vista)
            controlador.comenzar()
            SystemExit

# Tenemos un problema a la hora de hacer una reserva (se le puede poner el ID de una habitacion que no existe.)
# Hay que arreglar las regex para comprobar los datos en las clases.

