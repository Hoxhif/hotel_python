import IHabitaciones
class Habitaciones(IHabitaciones):
    
    __coleccion_habitaciones = []

    def get():
        copia_profunda = [i for i in Habitaciones.__coleccion_habitaciones]
        return copia_profunda
    
    def get_tamano():
        return len(Habitaciones.__coleccion_habitaciones)
    
    def insertar(habitacion):
        if habitacion is None:
            raise ValueError("No se puede insertar una habitación nula en la lista.")
        if Habitaciones.get().count(habitacion)>0:
            raise ValueError("No se puede insertar una habitación que ya existe.")
        Habitaciones.__coleccion_habitaciones.append(habitacion)

    def borrar(habitacion):
        if habitacion is None:
            raise ValueError("La habitación a borrar no puede ser nula.")
        if Habitaciones.get().count(habitacion)==0:
            raise ValueError("No existe la habitación a borrar.")
        Habitaciones.__coleccion_habitaciones.remove(habitacion)
    
    def buscar(habitacion):
        if habitacion is None:
            raise ValueError("La habitación a buscar no puede ser nulo.")
        if Habitaciones.get().count(habitacion)==0:
            raise ValueError("La habitación a buscar no existe.")
        return Habitaciones.get[Habitaciones.get().index(habitacion)]