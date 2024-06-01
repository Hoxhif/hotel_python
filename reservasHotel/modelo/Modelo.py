from modelo.negocio.IHuespedes import IHuespedes
from modelo.negocio.IHabitaciones import IHabitaciones
from modelo.negocio.IReservas import IReservas
class Modelo:

    def __init__(self):
        pass

    def comenzar(self):
        pass

    def terminar(self):
        print("Fin del programa.")

    def insertar_huesped(self, huesped):
        IHuespedes.insertar(self,huesped)

    def buscar_huesped(self, huesped):
        IHuespedes.buscar(self,huesped)

    def borrar_huesped(self, huesped):
        IHuespedes.borrar(self,huesped)

    def get_huespedes(self):
        return IHuespedes.get(self)

    def insertar_habitacion(self, habitacion):
        IHabitaciones.insertar(self,habitacion)

    def buscar_habitacion(self, habitacion):
        IHabitaciones.buscar(self,habitacion)

    def borrar_habitacion(self, habitacion):
        IHabitaciones.borrar(self,habitacion)

    def get_habitaciones(self):
        return IHabitaciones.get()

    def get_habitaciones_tipo_habitacion(self,tipo_habitacion):
        return IHabitaciones.get_tipo_habitacion(self,tipo_habitacion)

    def insertar_reserva(self,reserva):
        IReservas.insertar(self,reserva)

    def buscar_reserva(self,reserva):
        IReservas.buscar(self,reserva)

    def borrar_reserva(self,reserva):
        IReservas.borrar(self,reserva)

    def get_reservas(self):
        return IReservas.get(self)
    
    def get_reservas_huesped(self,huesped):
        return IReservas.get_reservas_por_huesped(self,huesped)

    def get_reservas_tipo_habitacion(self,tipo_habitacion):
        return IReservas.get_reservas_por_tipo_habitacion(self,tipo_habitacion)
        
    def get_reservas_futuras(self,habitacion):
        return IReservas.get_reservas_futuras(self,habitacion)

    def realizar_check_in(self,reserva, fecha):
        IReservas.realizar_check_in(self,reserva,fecha)

    def realizar_check_out(self,reserva, fecha):
        IReservas.realizar_check_out(self,reserva, fecha)
    