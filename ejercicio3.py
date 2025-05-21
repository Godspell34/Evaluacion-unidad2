"""
    Ejercicio #3: Simulación de una lista de reproducción de música. Implemente
una lista de reproducción de música utilizando una lista enlazada. El programa debe
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción,
reproducir la canción anterior y mostrar la lista de reproducción actual.
"""

class Cancion:
    """ Clase Cancion para representar una canción """
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None 
        
class ListaReproduccion:
    def __init__(self):
        self.cima = None
        self.cola = None
        self.cancion_actual = None   
        
    def agregar_cancion(self, nombre):
        """ Agrega una canción a la lista de reproducción """
        nueva_cancion = Cancion(nombre)
        if self.cima is None:
            self.cima = nueva_cancion
            self.cola = nueva_cancion
        else:
            self.cola.siguiente = nueva_cancion
            nueva_cancion.anterior = self.cola
            self.cola = nueva_cancion
        print(f"Canción '{nombre}' agregada a la lista de reproducción.")
        if self.cancion_actual is None:
            self.cancion_actual = nueva_cancion
            
    def eliminar_cancion(self, nombre):
        """ Elimina una canción de la lista de reproducción """
        if self.cima is None:
            print("La lista de reproducción está vacía.")
            return
        actual = self.cima
        while actual is not None:
            if actual.nombre == nombre:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cima = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                print(f"Canción '{nombre}' eliminada de la lista de reproducción.")
                return
            actual = actual.siguiente
        print(f"Canción '{nombre}' no encontrada en la lista de reproducción.")
    def reproducir_siguiente(self):
        """ Reproduce la siguiente canción en la lista de reproducción """
        if self.cancion_actual is None:
            print("No hay canciones en la lista de reproducción.")
            return
        print(f"Reproduciendo: {self.cancion_actual.nombre}")
        if self.cancion_actual.siguiente is not None:
            self.cancion_actual = self.cancion_actual.siguiente
        else:
            print("No hay más canciones en la lista de reproducción.")
    def reproducir_anterior(self):
        """ Reproduce la canción anterior en la lista de reproducción """
        if self.cancion_actual is None:
            print("No hay canciones en la lista de reproducción.")
            return
        print(f"Reproduciendo: {self.cancion_actual.nombre}")
        if self.cancion_actual.anterior is not None:
            self.cancion_actual = self.cancion_actual.anterior
        else:
            print("No hay más canciones en la lista de reproducción.")
    def mostrar_lista(self):
        """ Muestra la lista de reproducción actual """
        if self.cima is None:
            print("La lista de reproducción está vacía.")
            return
        actual = self.cima
        print("Lista de reproducción:")
        while actual is not None:
            print(f"- {actual.nombre}")
            actual = actual.siguiente

# Ejemplo de uso
if __name__ == "__main__":
    lista_reproduccion = ListaReproduccion()
    lista_reproduccion.agregar_cancion("Canción 1")
    lista_reproduccion.agregar_cancion("Canción 2")
    lista_reproduccion.agregar_cancion("Canción 3")
    
    lista_reproduccion.mostrar_lista()
    
    lista_reproduccion.reproducir_siguiente()
    lista_reproduccion.reproducir_anterior()
    
    lista_reproduccion.eliminar_cancion("Canción 2")
    
    lista_reproduccion.mostrar_lista()