from Opcion import Opcion
#from controlador.Controlador import Controlador as self
from Consola import Consola
class Vista:

    def set_controlador(self, controlador):
        if controlador is not None:
            self.__controlador=controlador
        else: raise ValueError("El controlador no puede ser nulo.")

    def get_controlador(self):
        return self.__controlador

    def comenzar(self):
        opcion=None
        while opcion!=Opcion.SALIR:
            Consola.mostrar_consola()
            opcion= Consola.elegir_opcion()
            self.ejecutar_opcion(opcion)
        SystemExit

    def terminar(self):
        self.__controlador.terminar()

    def ejecutar_opcion(self, opcion):
        match(opcion):
            case Opcion.SALIR: print("Fin del programa")
            case Opcion.INSERTAR_HUESPED: self.insertar_huesped()
            case Opcion.BUSCAR_HUESPED: self.buscar_huesped()
            case Opcion.BORRAR_HUESPED: self.borrar_huesped()
            case Opcion.MOSTRAR_HUESPEDES: self.mostrar_huespedes()
            case Opcion.INSERTAR_HABITACION: self.insertar_habitacion()
            case Opcion.BUSCAR_HABITACION: self.buscar_habitacion()
            case Opcion.BORRAR_HABITACION: self.borrar_habitacion()
            case Opcion.MOSTRAR_HABITACIONES: self.mostrar_habitacion()
            case Opcion.INSERTAR_RESERVA: self.insertar_reserva()
            case Opcion.MOSTRAR_RESERVAS: self.mostrar_reservas()
            case Opcion.ANULAR_RESERVA: self.anular_reserva()
            case Opcion.REALIZAR_CHECK_IN: self.realizar_check_in()
            case Opcion.REALIZAR_CHECK_OUT: self.realizar_check_out()
            case Opcion.CONSULTAR_DISPONIBILIDAD: self.consultar_disponibilidad()
    
    def insertar_huesped(self):
        huesped = Consola.leer_huesped()
        try:
            self.get_controlador().insertar_huesped(huesped)
            print("El huesped se ha insertado correctamente.")
        except ValueError as e:
            print(e)

    def buscar_huesped(self):
        huesped = Consola.leer_huesped_por_dni()
        print(huesped)

    def borrar_huesped(self):
        huesped = Consola.leer_huesped_por_dni()
        try:
            for i in self.get_controlador().get_huespedes():
                if i.get_dni() == huesped.get_dni():
                    self.get_controlador().borrar_huesped(i)
                    print("Se ha borrado el huesped correctamente.")
        except ValueError as e:
            print(e)
    
    def mostrar_huespedes(self):
        if len(self.get_controlador().get_huespedes())==0:
            print("No hay huespedes registrados.")
        else:
            for i in self.get_controlador().get_huespedes():
                print(i)

    def insertar_habitacion(self):
        habitacion = Consola.leer_habitacion()
        try:
            self.get_controlador().insertar_habitacion(habitacion)
            print("Se ha insertado la habitación correctamente.")
        except ValueError as e:
            print(e)

    def buscar_habitacion(self):
        habitacion = Consola.leer_habitacion_por_identificador()
        print(habitacion)

    def borrar_habitacion(self):
        habitacion = Consola.leer_habitacion_por_identificador()
        try:
            for i in self.get_controlador().get_habitaciones():
                if i.get_identificador() == habitacion.get_identificador():
                    self.get_controlador().borrar_habitacion(i)
                    print("Se ha borrado la habitación correctamente.")
        except ValueError as e:
            print(e)
    
    def mostrar_habitacion(self):
        if len(self.get_controlador().get_habitaciones())==0:
            print("No hay habitaciones registradas.")
        else:
            for i in self.get_controlador().get_habitaciones():
                print(i)
    
    def insertar_reserva(self):
        reserva = Consola.leer_reserva()
        try:
            self.get_controlador().insertar_reserva(reserva)
            print("Se ha insertado la reserva correctamente.")
        except ValueError as e:
            print(e)

    def mostrar_reservas(self):
        if len(self.get_controlador().get_reservas())==0:
            print("No hay reservas a mostrar.")
        else:
            print("Reservas a mostrar: ")
            print("1.- Todas las reservas.")
            print("2.- Reservas por Huesped.")
            print("3.- Reservas por Tipo de Habitacion")
            opcion = int(input("Seleccione la opcion: "))
            match(opcion):
                case 1: 
                    contador = 1
                    for i in self.get_controlador().get_reservas():
                        print(f"{contador}.- {i}")
                        contador+=1
                case 2: Vista.mostrar_reservas_huesped(self)
                case 3: Vista.mostrar_reservas_tipo_habitacion(self)

    def mostrar_reservas_huesped(self):
        huesped = Consola.leer_huesped_por_dni()
        contador=1
        try:
            if len(self.get_controlador().get_reservas_huesped(huesped))>0:
                for i in self.get_controlador().get_reservas_huesped(huesped):
                    print(f"{contador}.- {i}")
                    contador+=1
            else: print("El huesped no tiene ninguna reserva hecha.")
        except ValueError as e:
            print(e)
    
    def mostrar_reservas_tipo_habitacion(self):
        tipo = Consola.leer_tipo_habitacion()
        contador=1
        try:
            if len(self.get_controlador().get_reservas_tipo_habitacion(tipo))>0:
                for i in self.get_controlador().get_reservas_tipo_habitacion(tipo):
                    print(f"{contador}.- {i}")
                    contador+=1
            else: print("El tipo de habitación no tiene ninguna reserva hecha.")
        except ValueError as e:
            print(e)        

    def anular_reserva(self):
        huesped = Consola.leer_huesped_por_dni()
        contador=1
        try:
            if len(self.get_controlador().get_reservas_huesped(huesped))>0:
                for i in self.get_controlador().get_reservas_huesped(huesped):
                    print(f"{contador}.- {i}")
                    contador+=1
            else: print("El huesped no tiene ninguna reserva hecha.")
            opcion = int(input("Seleccione la reserva a borrar: "))
            reserva = self.get_controlador().get_reservas_huesped(huesped)[opcion-1]
            self.get_controlador().borrar_reserva(reserva)
            print("Se ha borrado la reserva correctamente.")
        except ValueError as e:
            print(e) 
        
    def consultar_disponibilidad(self): # True habitacion disponible # False habitación no disponible
        habitacion = Consola.leer_habitacion_por_identificador()
        inicio = Consola.leer_fecha("Inserte la posible fecha de inicio de reserva en la habitación: ")
        fin = Consola.leer_fecha("Inserte la posible fecha de fin de reserva en la habitación: ")
        reservas_futuras = self.get_controlador().get_reservas_futuras(habitacion)
        consulta: bool
        if len(reservas_futuras) == 0:
            consulta=True
        else:
            reservas_futuras = sorted(reservas_futuras, key=lambda reserva: reserva.get_fecha_fin())
            if inicio>reservas_futuras[0].get_fecha_inicio():
                consulta= True
            else:
                reservas_futuras = sorted(reservas_futuras,key=lambda reserva: reserva.get_fecha_inicio())
                if fin< reservas_futuras[0].get_fecha_fin():
                    consulta= True
                else:
                    if inicio>reservas_futuras[0].get_fecha_fin() and fin<reservas_futuras[0].get_fecha_inicio():
                        consulta= True
                    else: consulta= False
        if consulta:
            print(f"La habitación estará disponible entre los días {inicio} y {fin}")
        else: print(f"La habitación no está disponible entre los días {inicio} y {fin}")

    def realizar_check_in(self):
        dni = input("Inserte el DNI del huesped para mostrar sus reservas: ")
        for i in self.get_controlador().get_huespedes():
            if i.get_dni() == dni:
                huesped = i
        print("Seleccione la Reserva del Huesped a realizar el check-in")
        contador=1
        if len(self.get_controlador().get_reservas_huesped(huesped))>0:
            for i in self.get_controlador().get_reservas_huesped(huesped):
                print(f"{contador}.- {i}")
                contador+=1
        #Vista.mostrar_reservas_huesped(huesped)
            opcion = int(input("Seleccione la reserva a realizar el check-in: "))
            reserva = self.get_controlador().get_reservas_huesped(huesped)[opcion-1]
            #fecha = input("Indique la fecha del check-in (formato dd/MM/yyyy HH:mm:ss): ")
            fecha = Consola.leer_fecha_hora("Inserte la fecha para realizar el Check-In: ")
            self.get_controlador().realizar_check_in(reserva, fecha)
        else: print("El huesped no tiene ninguna reserva para realizar Check-In.")
        

    def realizar_check_out(self):
        dni = input("Inserte el DNI del huesped para mostrar sus reservas: ")
        for i in self.get_controlador().get_huespedes():
            if i.get_dni() == dni:
                huesped = i
        print("Seleccione la Reserva del Huesped a realizar el check-out")
        contador=1
        if len(self.get_controlador().get_reservas_huesped(huesped))>0:
            for i in self.get_controlador().get_reservas_huesped(huesped):
                print(f"{contador}.- {i}")
                contador+=1
            opcion = int(input("Seleccione la reserva a realizar el check-out: "))
            reserva = self.get_controlador().get_reservas_huesped(huesped)[opcion-1]
            fecha = input ("Indique la fecha del check-out (formato dd/MM/yyyy HH:mm:ss): ")
            self.get_controlador().realizar_check_out(reserva, fecha)
        else: print("El huesped no tiene ninguna reserva para realizar check-out")