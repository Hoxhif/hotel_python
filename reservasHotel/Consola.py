from Opcion import Opcion
from modelo.dominio.Huesped import Huesped
from modelo.dominio.Habitacion import Habitacion
from modelo.dominio.Reserva import Reserva
from modelo.dominio.TipoHabitacion import TipoHabitacion
from modelo.dominio.Regimen import Regimen
from modelo.negocio.IHuespedes import IHuespedes
from modelo.negocio.IHabitaciones import IHabitaciones
from modelo.dominio.Doble import Doble
from modelo.dominio.Suite import Suite
from modelo.dominio.Triple import Triple
from modelo.dominio.Simple import Simple
import re as regex
from datetime import date
import datetime
import copy
class Consola:

    def mostrar_consola():
        contador=1
        for i in Opcion:
            print(f"{contador}: {i}")
            contador+=1
    
    def elegir_opcion():
        eleccion=False
        while not eleccion:
            eleccion = int(input("Seleccione una opción: "))
            opciones = list(Opcion)
            if 1<= eleccion <= len(opciones):
                opcion = opciones[eleccion-1] # Los enum no funcionan con indices
                return opcion
            else: print("La opción seleccionada no es válida.")
            
    
    def leer_huesped():
        nombre = input("Inserte el nombre del Huesped: ")
        
        dni = input("Inserte el DNI del Huesped: ")
        telefono = input("Inserte el teléfono del Huesped: ")
        correo = input("Inserte el correo del Huesped: ")
        fecha_nac = Consola.leer_fecha("Inserte la fecha de nacimiento del Huesped: ")
        try:
            
            return Huesped(nombre, dni, correo, telefono, fecha_nac)
        except ValueError as e:
            print(e)
            Consola.leer_huesped()

    def leer_huesped_por_dni():
        dni = input("Introduce el DNI del Huesped: ")
        for i in IHuespedes.get():
            if i.get_dni() == dni:
                return copy.copy(i)
                #return Huesped(huesped=i)
        print("No se ha encontrado al Huesped.")
            
    def leer_fecha(texto):
        fecha = input(texto)
        empaquetado = tuple(fecha.split("/"))
        fecha = date(int(empaquetado[2]), int(empaquetado[1]), int(empaquetado[0]))
        return fecha
    
    def leer_fecha_hora(texto):
        patron = r'[:/ ]' # Uso de expresion regular para hacer esta parte.
        fecha= input(texto)
        empaquetado = tuple(regex.split(patron,fecha))
        print(empaquetado)
        fecha = datetime.datetime(int(empaquetado[2]), int(empaquetado[1]), int(empaquetado[0]), int(empaquetado[3]), int(empaquetado[4]), int(empaquetado[5]))
        return fecha

    def leer_habitacion():
        planta=int(input("Inserte la planta de la Habitación: "))
        puerta=int(input("Inserte la puerta de la Habitación: "))
        precio=float(input("Inserte el precio de la Habitación: "))
        tipo = Consola.leer_tipo_habitacion()
        match(tipo):
            case TipoHabitacion.SIMPLE: 
                try:
                    return Simple(planta, puerta, precio)
                except ValueError as e:
                    print(e)
                    Consola.leer_habitacion()
            case TipoHabitacion.DOBLE:
                try:
                    camas_individuales=int(input("Inserte el número de camas individuales: "))
                    camas_dobles=int(input("Inserte el número de camas dobles:  "))
                    return Doble(planta, puerta, precio, camas_individuales, camas_dobles)
                except ValueError as e:
                    print(e)
                    Consola.leer_habitacion()
            case TipoHabitacion.TRIPLE:
                try:
                    camas_individuales=int(input("Inserte el número de camas individuales: "))
                    camas_dobles=int(input("Inserte el número de camas dobles:  "))
                    num_banos = int(input("Inserte el número de baños:  "))
                    return Triple(planta, puerta, precio, camas_individuales, camas_dobles,num_banos)
                except ValueError as e:
                    print(e)
                    Consola.leer_habitacion()
            case TipoHabitacion.SUITE:
                    num_banos = int(input("Inserte el número de baños:  "))
                    jacuzzi = input("Inserte si tendrá jacuzzi la habitación o no (S/n): ")
                    if jacuzzi == "S":
                         try:
                            return Suite(planta, puerta, precio,num_banos,True)
                         except ValueError as e:
                            print(e)
                            Consola.leer_habitacion()
                    else:
                        try:
                            return Suite(planta, puerta, precio,num_banos,False)
                        except ValueError as e:
                            print(e)
                            Consola.leer_habitacion()
    
    def leer_habitacion_por_identificador():
        identificador = input("Inserte el ID de la Habitación: ")
        for i in IHabitaciones.get():
            if i.get_identificador() == identificador:
                return copy.copy(i)
                #return Habitacion(habitacion=i)
        print("No se ha encontrado la habitación")
    
    def leer_tipo_habitacion():
        counter=1
        for i in TipoHabitacion:
            print(f"{counter}.- {i.value[0]}")
            counter+=1
        seleccion = int(input("Seleccione el tipo de habitación de la Habitación: "))
        opciones = list(TipoHabitacion)
        if 1<= seleccion <= len(opciones):
            try:
                return opciones[seleccion-1]
            except IndexError as e:
                print(e)
                Consola.leer_tipo_habitacion()
            

    def leer_regimen():
        contador=1
        for i in Regimen:
            print(f"{contador}.- {i}")
            contador+=1
        seleccion = int(input("Seleccione el tipo de régimen de la reserva: "))
        opciones = list(Regimen)
        if 1<= seleccion <= len(opciones):
            try:
                return opciones[seleccion-1]
            except IndexError as e:
                print(e)
                Consola.leer_regimen()
            
    

    def leer_reserva():
        huesped = input("Inserte el DNI del Huesped: ")
        for i in IHuespedes.get():
            if i.get_dni() == huesped:
                huesped = i
        habitacion = input("Inserte el ID de la habitación: ")
        for i in IHabitaciones.get():
            if i.get_identificador() == habitacion:
                habitacion = i
        regimen = Consola.leer_regimen()
        fecha_inicio = Consola.leer_fecha("Inserte la fecha de inicio de reserva: ")
        fecha_fin = Consola.leer_fecha("Inserte la fecha de fin de reserva: ")
        num_personas = int(input("Inserte el número de personas en la reserva: "))
        try:
            return Reserva(huesped, habitacion, regimen, fecha_inicio, fecha_fin, num_personas)
        except ValueError as e:
            print(e)
            Consola.leer_reserva()




