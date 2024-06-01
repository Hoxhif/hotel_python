from enum import Enum
#from abc import ABC, abstractmethod
'''
class OpcionBase(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def set_vista(self, vista):
        pass
        


        def __init__(self):
        self.__vista_opcion=None

    def set_vista(self, vista):
        self.__vista_opcion = vista

    def ejecutar(self):
        if self.__vista_opcion==None:
            raise ValueError("Vista no establecida para la opción.")
        if self.__vista_opcion== Opcion.SALIR:
            self.__vista_opcion.terminar()
        if self.__vista_opcion== Opcion.INSERTAR_HUESPED:
            self.__vista_opcion.insertar_huesped()
        if self.__vista_opcion== Opcion.BUSCAR_HUESPED:
            self.__vista_opcion.buscar_huesped()
        if self.__vista_opcion== Opcion.BORRAR_HUESPED:
            self.__vista_opcion.borrar_huesped()
        if self.__vista_opcion== Opcion.INSERTAR_HABITACION:
            self.__vista_opcion.insertar_habitacion()
        if self.__vista_opcion== Opcion.BUSCAR_HABITACION:
            self.__vista_opcion.buscar_habitacion()
        if self.__vista_opcion== Opcion.BORRAR_HABITACION:
            self.__vista_opcion.borrar_habitacion()
        if self.__vista_opcion== Opcion.MOSTRAR_HUESPEDES:
            self.__vista_opcion.mostrar_huespedes()
        if self.__vista_opcion== Opcion.MOSTRAR_HABITACIONES:
            self.__vista_opcion.mostrar_habitaciones()
        if self.__vista_opcion== Opcion.INSERTAR_RESERVA:
            self.__vista_opcion.insertar_reserva()
        if self.__vista_opcion== Opcion.ANULAR_RESERVA:
            self.__vista_opcion.anular_reserva()
        if self.__vista_opcion== Opcion.MOSTRAR_RESERVAS:
            self.__vista_opcion.mostrar_reservas()
        if self.__vista_opcion== Opcion.REALIZAR_CHECK_IN:
            self.__vista_opcion.realizar_check_in()
        if self.__vista_opcion== Opcion.REALIZAR_CHECK_OUT:
            self.__vista_opcion.realizar_check_out()
        if self.__vista_opcion== Opcion.CONSULTAR_DISPONIBILIDAD:
            self.__vista_opcion.consultar_disponibilidad()
            
        


'''
class Opcion(Enum):
    SALIR = "Salir"
    INSERTAR_HUESPED= "Insertar Huesped"
    BUSCAR_HUESPED = "Buscar Huesped"
    BORRAR_HUESPED = "Borrar Huesped"
    MOSTRAR_HUESPEDES = "Mostrar Huespedes"
    INSERTAR_HABITACION = "Insertar Habitación"
    BUSCAR_HABITACION = "Buscar Habitación"
    BORRAR_HABITACION = "Borrar Habitación"
    MOSTRAR_HABITACIONES = "Mostrar Habitaciones"
    INSERTAR_RESERVA = "Insertar Reserva"
    ANULAR_RESERVA = "Anular Reserva"
    MOSTRAR_RESERVAS = "Mostrar Reservas"
    REALIZAR_CHECK_IN = "Realizar Check-In"
    REALIZAR_CHECK_OUT = "Realizar Check-Out"
    CONSULTAR_DISPONIBILIDAD = "Consultar Disponibilidad"

    
    def __str__(self):
        return self.value
