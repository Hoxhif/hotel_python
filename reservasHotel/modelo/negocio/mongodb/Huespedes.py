import IHuespedes
class Huespedes(IHuespedes):
    __coleccion_huespedes = [] #Al ser static no hago constructor.

    def get():
        copia_profunda = [i for i in Huespedes.__coleccion_huespedes]
        return copia_profunda
    
    def get_tamano(cls): #cls es como pasarle Huespedes clase en si, no la instancia de Huesped como sería self
        return len(Huespedes.__coleccion_huespedes)
    
    def insertar(huesped):
        if huesped is None:
            raise ValueError("No se puede insertar un huesped nulo en la lista.")
        if Huespedes.get().count(huesped)>0:
            raise ValueError("No se puede insertar un huesped que ya existe.")
        Huespedes.__coleccion_huespedes.append(huesped)

    def borrar(huesped):
        if huesped is None:
            raise ValueError("El huesped a borrar no puede ser nulo.")
        if Huespedes.get().count(huesped)==0:
            raise ValueError("No existe el huesped a borrar.")
        Huespedes.__coleccion_huespedes.remove(huesped)
    
    def buscar(huesped):
        if huesped is None:
            raise ValueError("El huesped a buscar no puede ser nulo.")
        if Huespedes.get().count(huesped)==0:
            raise ValueError("El huesped a buscar no existe.")
        return Huespedes.get[Huespedes.get().index(huesped)]
    
    
