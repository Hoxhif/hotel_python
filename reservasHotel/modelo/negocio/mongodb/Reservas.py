from datetime import date
import IReservas
class Reservas(IReservas):
    __coleccion_reservas = []
        
    def get():
        copia_profunda = [i for i in Reservas.__coleccion_reservas]
        return copia_profunda
    
    def get_tamano():
        return len(Reservas.__coleccion_reservas)
    
    def insertar(reserva):
        if reserva is None:
            raise ValueError("No se puede insertar una reserva nula en la lista.")
        if Reservas.get().count(reserva)>0:
            raise ValueError("No se puede insertar una reserva que ya existe.")
        Reservas.__coleccion_reservas.append(reserva)

    def borrar(reserva):
        if reserva is None:
            raise ValueError("La reserva a borrar no puede ser nula.")
        if Reservas.get().count(reserva)==0:
            raise ValueError("No existe la reserva a borrar.")
        Reservas.__coleccion_reservas.remove(reserva)
    
    def buscar(reserva):
        if reserva is None:
            raise ValueError("La reserva a buscar no puede ser nulo.")
        if Reservas.get().count(reserva)==0:
            raise ValueError("La reserva a buscar no existe.")
        return Reservas.get[Reservas.get().index(reserva)]
    
    def get_reservas_por_huesped(huesped):
        if huesped == None:
            raise ValueError("El huesped no puede ser nulo.")
        copia_reservas = []
        for i in Reservas.get():
            if i.get_huesped().get_dni() == huesped.get_dni():
                copia_reservas.append(i)
        return copia_reservas
    
    def get_reservas_por_tipo_habitacion(tipo_habitacion):
        if tipo_habitacion == None:
            raise ValueError("El tipo de habitación no puede ser nulo.")
        copia_reservas = []
        for i in Reservas.get():
            if i.get_habitacion().get_tipo_habitacion() == tipo_habitacion:
                copia_reservas.append(i)
        return copia_reservas
    
    def get_reservas_futuras(habitacion):
        if habitacion == None:
            raise ValueError("La habitación no puede ser nula.")
        copia_reservas = []
        fecha_ahora = date.today()
        for i in Reservas.get():
            if i.get_habitacion().get_identificador() == habitacion.get_identificador():
                if  i.get_fecha_inicio() > fecha_ahora:
                    copia_reservas.append(i)
        return copia_reservas
    
    def realizar_check_in(reserva, fecha):
        if reserva.get_check_in() is None:
            reserva.set_check_in(fecha)
        else:
            raise ValueError("La reserva ya tiene hecho un check-in")

    def realizar_check_out(reserva, fecha):
        if reserva.get_check_out() is None:
            reserva.set_check_out(fecha)
        else: 
            raise ValueError("La reserva ya tiene hecho un check-out")