from abc import ABC, abstractmethod
class IHabitaciones(ABC):

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def get_tamano():
        pass

    @abstractmethod
    def insertar(huesped):
        pass

    @abstractmethod
    def buscar(huesped):
        pass

    @abstractmethod
    def borrar(huesped):
        pass