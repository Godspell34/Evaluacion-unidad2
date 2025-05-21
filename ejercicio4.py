""" Ejercicio #4: Implementación de una cola de prioridad. Diseñe una cola de
prioridad donde los elementos se desencolan según su prioridad. Cada elemento
tendrá un nombre y una prioridad (un número entero, donde un número menor indica
mayor prioridad)."""

class Nodo:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def insertar(self, nombre, prioridad):
        nuevo = Nodo(nombre, prioridad)

        # Si la cola está vacía o la prioridad del nuevo nodo es menor (más importante)
        if self.frente is None or prioridad < self.frente.prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print(f"Elemento '{nombre}' con prioridad {prioridad} insertado.")

    def eliminar(self):
        if self.frente is None:
            print("La cola de prioridad está vacía.")
            return None
        eliminado = self.frente
        self.frente = self.frente.siguiente
        print(f"Elemento '{eliminado.nombre}' con prioridad {eliminado.prioridad} eliminado.")
        return eliminado

    def mostrar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return
        actual = self.frente
        print("Cola de prioridad actual:")
        while actual:
            print(f"  - {actual.nombre} (Prioridad {actual.prioridad})")
            actual = actual.siguiente

# Ejemplo de uso
cola = ColaPrioridad()
cola.insertar("Tarea A", 3)
cola.insertar("Tarea B", 1)
cola.insertar("Tarea C", 2)

cola.mostrar()
cola.eliminar()
cola.mostrar()