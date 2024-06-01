from abc import ABC, abstractmethod
class Habitacion(ABC): # Esto se pone para clases abstractas (ABC Abstract Base Class)

    def __init__(self, planta, puerta, precio):
        if (planta, puerta, precio) != None:
            self.__set_planta(planta)
            self.__set_puerta(puerta)
            self.__set_precio(precio)
            self.__set_identificador()
        else:
            raise Exception("Error al usar el constructor de Habitación")

    @abstractmethod
    def get_numero_maximo_personas():
        pass
    
    def get_identificador(self):
        return self.__identificador
    
    def get_planta(self):
        return self.__planta
    
    def get_puerta(self):
        return self.__puerta
    
    def get_precio(self):
        return self.__precio
    
    def __set_identificador(self,identificador:int=None):
            if identificador==None:
                self.__identificador = str(self.get_planta())+str(self.get_puerta())
            else:
                self.__identificador= identificador

    def __set_planta(self, planta:int):
        if planta < 1 or planta > 3:
            raise ValueError("La planta no puede ser mayor de 3 ni menor de 1.")
        self.__planta = planta

    def __set_puerta(self, puerta:int):
        if puerta < 1 or puerta > 15:
            raise ValueError("La puerta no puede ser mayor de 15 ni menor de 1.")
        self.__puerta=puerta

    def __set_precio(self, precio:float):
        if precio<40 or precio>150:
            raise ValueError("El precio de la habitación no puede ser mayor a 150 o menor a 40.")
        self.__precio = precio


    def __str__(self):
        return f"Habitación en la Planta {self.get_planta()} y Puerta {self.get_puerta()} (ID: {self.get_identificador()}), precio: {self.get_precio()}"
    
    def __eq__(self, other):
        if isinstance(other, Habitacion):
            return self.__identificador == other.get_identificador()
        return False
    
    def __hash__(self):
        return hash(self.__identificador)