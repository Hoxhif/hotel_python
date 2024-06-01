import re as regex
class Reserva:
    def __init__(self, huesped=None, habitacion=None, regimen=None, fecha_inicio=None, fecha_fin=None, num_personas=None):
        if (huesped, habitacion, regimen, fecha_inicio,fecha_fin, num_personas) != None:
            self.__set_huesped(huesped)
            self.__set_habitacion(habitacion)
            self.__set_regimen(regimen)
            self.__set_fecha_inicio(fecha_inicio)
            self.__set_fecha_fin(fecha_fin)
            self.__set_num_personas(num_personas)
            self.__precio=0
            self.__check_in=None
            self.__check_out=None
        else:
            raise Exception("Error al usar el constructor de Reserva.")

    def get_huesped(self):
        return self.__huesped
    
    def get_habitacion(self):
        return self.__habitacion
    
    def get_regimen(self):
        return self.__regimen
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_fecha_fin(self):
        return self.__fecha_fin
    
    def get_check_in(self):
        return self.__check_in
    
    def get_check_out(self):
        return self.__check_out
    
    def get_precio(self):
        return self.__precio
    
    def get_num_personas(self):
        return self.__num_personas
    
    def __set_huesped(self, huesped):
        if huesped == None:
            raise ValueError("Un huesped no puede ser nulo.")
        self.__huesped=huesped
    
    def __set_habitacion(self, habitacion):
        if habitacion == None:
            raise ValueError("Una habitación no puede ser nula.")
        self.__habitacion= habitacion

    def __set_regimen(self, regimen):
        if regimen == None:
            raise ValueError("El régimen no puede ser nulo.")
        self.__regimen = regimen
    
    def __set_fecha_inicio(self, fecha_inicio):
        if fecha_inicio == None:
            raise ValueError("La fecha de inicio no puede ser nula.")
        self.__fecha_inicio=fecha_inicio
    
    def __set_fecha_fin(self, fecha_fin):
        if fecha_fin == None:
            raise ValueError("La fecha de fin no puede ser nula.")
        self.__fecha_fin=fecha_fin

    def __set_num_personas(self, num_personas):
        if num_personas<1 or num_personas>5:
            raise ValueError("El numero de personas solo puede entre 1 a 5")
        self.__num_personas = num_personas

    def get_check_in(self):
        return self.__check_in

    def get_check_out(self):
        return self.__check_out

    def __set_precio(self):
        self.__precio = (self.get_habitacion().get_precio() + self.get_regimen().value[1]) * self.get_num_personas()
    
    def set_check_in(self, check_in):
        if check_in == None:
            raise ValueError("La fecha del Check In no puede ser nula.")
        ''' A ARREGLAR: 
        fecha_string = check_in.strftime("%d/%m/%Y %H:%M:%S")
        print(fecha_string)
        validador = self.regex.match(string=fecha_string, pattern="dd/MM/yyyy HH:mm:ss")
        if validador == None:
            raise ValueError("La fecha de Check-In no tiene un formato correcto (dd/MM/yyyy HH:mm:ss).")
        '''
        self.__check_in = check_in
    
    def set_check_out(self, check_out):
        if check_out == None:
            raise ValueError("La fecha del Check Out no puede ser nula.")
        self.__check_out = check_out
        self.__set_precio()

    def __str__(self):
        if self.get_check_in()==None:
            cadena_checkin = "No Registrado"
        else: cadena_checkin = self.get_check_in()
        if self.get_check_out()==None:
            cadena_checkout= "No Registrado"
        else: cadena_checkout= self.get_check_out()
        return f"Información del huesped: {self.get_huesped()} | Información de la habitación: {self.get_habitacion()} |Régimen: {self.get_regimen()} ,Fecha de Inicio: {self.get_fecha_inicio()}, Fecha de Fin: {self.get_fecha_fin()}, Check-IN: {cadena_checkin}, Check-Out: {cadena_checkout}, Precio: {self.get_precio()} ,Número de Personas: {self.get_num_personas()}"
    
    def __eq__(self, other):
        if self is other:
            return True
        return self == other
    
    def __hash__(self):
        return hash(self.__huesped, self.__habitacion)