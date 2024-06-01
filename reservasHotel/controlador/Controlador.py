class Controlador:

    def __init__(self, modelo, vista):
        if modelo == None:
            raise ValueError("El modelo no puede ser nulo.")
        if vista == None:
            raise ValueError("La vista no puede ser nula.")
        self.__modelo=modelo
        self.__vista=vista
        self.__vista.set_controlador(self)
        
    def comenzar(self):
        self.__modelo.comenzar()
        self.__vista.comenzar()

    def terminar(self):
        print("Fin del programa.")

    def insertar_huesped(self, huesped):
        self.__modelo.insertar_huesped(huesped)

    def buscar_huesped(self,huesped):
        self.__modelo.buscar_huesped(huesped)

    def borrar_huesped(self,huesped):
        self.__modelo.borrar_huesped(huesped)

    def get_huespedes(self):
        return self.__modelo.get_huespedes()

    def insertar_habitacion(self,habitacion):
        self.__modelo.insertar_habitacion(habitacion)

    def buscar_habitacion(self,habitacion):
        self.__modelo.buscar_habitacion(habitacion)

    def borrar_habitacion(self,habitacion):
        self.__modelo.borrar_habitacion(habitacion)

    def get_habitaciones(self):
        return self.__modelo.get_habitaciones()

    def get_habitaciones_tipo_habitacion(self,tipo_habitacion):
        return self.__modelo.get_habitaciones_tipo_habitacion(tipo_habitacion)

    def insertar_reserva(self,reserva):
        self.__modelo.insertar_reserva(reserva)

    def buscar_reserva(self,reserva):
        self.__modelo.buscar_reserva(reserva)

    def borrar_reserva(self,reserva):
        self.__modelo.borrar_reserva(reserva)

    def get_reservas(self):
        return self.__modelo.get_reservas()
    
    def get_reservas_huesped(self,huesped):
        return self.__modelo.get_reservas_huesped(huesped)

    def get_reservas_tipo_habitacion(self,tipo_habitacion):
        return self.__modelo.get_reservas_tipo_habitacion(tipo_habitacion)
        
    def get_reservas_futuras(self,habitacion):
        return self.__modelo.get_reservas_futuras(habitacion)

    def realizar_check_in(self,reserva, fecha):
        self.__modelo.realizar_check_in(reserva,fecha)

    def realizar_check_out(self,reserva, fecha):
        self.__modelo.realizar_check_out(reserva, fecha)