from abc import ABC, abstractmethod
class IReservas(ABC):

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def get_tipo_habitacion():
        pass

    @abstractmethod
    def get_tamano():
        pass

    @abstractmethod
    def insertar(reserva):
        pass

    @abstractmethod
    def buscar(reserva):
        pass

    @abstractmethod
    def borrar(reserva):
        pass

    @abstractmethod
    def get_reservas_por_huesped(huesped):
        pass

    @abstractmethod
    def get_reservas_por_tipo_habitacion(tipo_habitacion):
        pass

    @abstractmethod
    def get_reservas_futuras(habitacion):
        pass

    @abstractmethod
    def realizar_check_in(reserva, fecha):
        pass

    @abstractmethod
    def realizar_check_out(reserva, fecha):
        pass