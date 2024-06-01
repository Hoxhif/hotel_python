from abc import ABC, abstractmethod
from typing import List
from modelo.dominio.Huesped import Huesped
class IHuespedes(ABC):

    @abstractmethod
    def get(self) -> List[Huesped]:
        pass

    @abstractmethod
    def get_tamano(self) -> int:
        pass

    @abstractmethod
    def insertar(self,huesped):
        pass

    @abstractmethod
    def buscar(self,huesped):
        pass

    @abstractmethod
    def borrar(self,huesped):
        pass

    