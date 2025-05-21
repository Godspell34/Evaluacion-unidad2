"""Ejercicio #5: Búsqueda en una lista enlazada. Cree una función que busque un
valor específico en una lista enlazada. La función debe devolver la posición del valor
si se encuentra, o un mensaje indicando que el valor no está en la lista."""

def buscar_en_lista_enlazada(lista, valor):
    """
    Busca un valor específico en una lista enlazada.

    Args:
        lista (LinkedList): La lista enlazada en la que se busca el valor.
        valor: El valor a buscar en la lista.

    Returns:
        int: La posición del valor si se encuentra, o -1 si no se encuentra.
    """
    posicion = 0
    nodo_actual = lista.cabeza

    while nodo_actual is not None:
        if nodo_actual.dato == valor:
            return posicion
        nodo_actual = nodo_actual.siguiente
        posicion += 1

    return -1

# Ejemplo de uso
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class LinkedList:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
# Crear una lista enlazada y agregar algunos elementos
lista = LinkedList()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
# Buscar un valor en la lista enlazada
valor_a_buscar = 20
posicion = buscar_en_lista_enlazada(lista, valor_a_buscar)

if posicion != -1:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")