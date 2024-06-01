import copy
class Huesped:
    import re as regex
    def __init__(self, nombre, dni, correo, telefono, fecha_nacimiento):
        if (nombre, dni, correo, telefono , fecha_nacimiento) != None:
            self.__set_nombre(nombre)
            self.__set_dni(dni)
            self.__set_correo(correo)
            self.__set_telefono(telefono)
            self.__set_fecha_nacimiento(fecha_nacimiento)

        else:
            raise Exception("Error al usar el constructor de Huesped.")
        

    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_correo(self):
        return self.__correo
    
    def get_telefono(self):
        return self.__telefono
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def __set_nombre(self, nombre):
        if nombre == None:
            raise ValueError("El valor del nombre no puede ser nulo.")
        if nombre.isspace():
            raise ValueError("El nombre no puede ser una cadena vacia.")
        validador = self.regex.match("[A-Za-z]+", nombre)
        if validador == None:
            raise ValueError("El formato de nombre no es correcto.")
        self.__nombre = self.__formatea_nombre(nombre)

    def __set_dni(self, dni):
        if dni == None:
            raise ValueError("El valor del dni no puede ser nulo.")
        if dni.isspace():
            raise ValueError("El nombre no puede ser una cadena vacia.")
        validador = self.regex.match("[0-9]{8}[A-Z]", dni)
        if validador == None:
            raise ValueError("El formato de DNI no es correcto.")
        if not self.__comprobar_letra_dni(dni):
            raise ValueError("La letra del DNI no corresponde a un DNI real.")
        self.__dni = dni
        
    def __set_correo(self, correo):
        if correo == None:
            raise ValueError("El valor del correo no puede ser nulo.")
        if correo.isspace():
            raise ValueError("El nombre no puede ser una cadena vacia.")
        validador = self.regex.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", correo)
        if validador == None:
            raise ValueError("El formato de correo no es correcto.")
        self.__correo = correo

    def __set_telefono(self, telefono):
        if telefono == None:
            raise ValueError("El valor del telefono no puede ser nulo.")
        if telefono.isspace():
            raise ValueError("El nombre no puede ser una cadena vacia.")
        validador = self.regex.match("[0-9]{9}", telefono)
        if validador == None:
            raise ValueError("El formato de telefono no es correcto.")
        self.__telefono = telefono

    def __set_fecha_nacimiento(self, fecha_nacimiento):
        if fecha_nacimiento == None: 
            raise ValueError("El valor de la fecha de nacimiento no puede ser nulo.")
        self.__fecha_nacimiento = fecha_nacimiento

    def __formatea_nombre(self,nombre: str):
        nombre_formateado = nombre
        division_nombre = nombre_formateado.split(" ")
        nombre_formateado= ""
        aux=""
        for i in division_nombre:
            aux=i
            aux=aux.capitalize()
            nombre_formateado+= aux+ " "
        return nombre_formateado
    
    def __comprobar_letra_dni(self,dni: str):
        num_dni=""
        for i in dni:
            if i.isdigit():
                num_dni+= i
        num_dni = int(num_dni)
        num_dni = num_dni%23
        match(num_dni):
            case 0:return dni[-1] == "T"
            case 1: return dni[-1] == "R"
            case 2: return dni[-1] == "W"
            case 3: return dni[-1] == "A"
            case 4: return dni[-1] == "G"
            case 5: return dni[-1] == "M"
            case 6: return dni[-1] == "Y"
            case 7: return dni[-1] == "F"
            case 8: return dni[-1] == "P"
            case 9: return dni[-1] == "D"
            case 10: return dni[-1] == "X"
            case 11: return dni[-1] == "B"
            case 12: return dni[-1] == "N"
            case 13: return dni[-1] == "J"
            case 14: return dni[-1] == "Z"
            case 15: return dni[-1] == "S"
            case 16: return dni[-1] == "Q"
            case 17: return dni[-1] == "V"
            case 18: return dni[-1] == "H"
            case 19: return dni[-1] == "L"
            case 20: return dni[-1] == "C"
            case 21: return dni[-1] == "K"
            case 22: return dni[-1] == "E"
    
    def __get_iniciales(self):
        iniciales = self.get_nombre().split(" ")
        get_iniciales= ""
        for i in iniciales:
            for j in i:
                if j.isupper():
                    get_iniciales+= j
        return get_iniciales
    
    def __str__(self):
        return f"Huesped: {self.get_nombre()} ({self.__get_iniciales()}), DNI: {self.get_dni()}, Correo: {self.get_correo()}, Teléfono: {self.get_telefono()}, Fecha de Nacimiento: {self.get_fecha_nacimiento()}"
    
    def __eq__(self, other):
        if isinstance(other, Huesped):
            return self.__dni == other.get_dni()
        return False
    
    def __hash__(self):
        return hash(self.__dni)



