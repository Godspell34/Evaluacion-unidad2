class Nodo:
    """
    Clase que representa un nodo en una estructura de datos enlazada.
    
    Cada nodo contiene un valor (dato) y una referencia al siguiente nodo.
    """
    
    def __init__(self, dato):
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            dato: El valor que almacenará el nodo.
        """
        self.dato = dato
        self.siguiente = None


class Pila:
    """
    Implementación de una estructura de datos tipo pila (stack) en Python usando nodos enlazados.
    
    Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out),
    lo que significa que el último elemento añadido es el primero en ser eliminado.
    
    Esta implementación utiliza nodos enlazados en lugar de listas para almacenar los elementos.
    
    Operaciones principales:
    - push: añade un elemento al tope de la pila
    - pop: elimina y devuelve el elemento del tope de la pila
    - peek: devuelve el elemento del tope sin eliminarlo
    - esta_vacia: verifica si la pila está vacía
    """
    
    def __init__(self):
        """Inicializa una pila vacía."""
        self.tope = None  # El tope de la pila (nodo superior)
        self.tamano_actual = 0  # Contador para el número de elementos
    
    def push(self, item):
        """
        Añade un elemento al tope de la pila.
        
        Args:
            item: El elemento a añadir a la pila.
        """
        nuevo_nodo = Nodo(item)  # Crear un nuevo nodo con el elemento
        nuevo_nodo.siguiente = self.tope  # El siguiente del nuevo nodo es el tope actual
        self.tope = nuevo_nodo  # El nuevo nodo se convierte en el tope
        self.tamano_actual += 1  # Incrementar el contador de tamaño
    
    def pop(self):
        """
        Elimina y devuelve el elemento del tope de la pila.
        
        Returns:
            El elemento del tope de la pila.
            
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("No se puede hacer pop() de una pila vacía")
        
        dato = self.tope.dato  # Guardar el dato del tope
        self.tope = self.tope.siguiente  # El tope pasa a ser el siguiente nodo
        self.tamano_actual -= 1  # Decrementar el contador de tamaño
        return dato
    
    def peek(self):
        """
        Devuelve el elemento del tope sin eliminarlo.
        
        Returns:
            El elemento del tope de la pila.
            
        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("No se puede hacer peek() de una pila vacía")
        
        return self.tope.dato
    
    def esta_vacia(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            True si la pila está vacía, False en caso contrario.
        """
        return self.tope is None
    
    def tamano(self):
        """
        Devuelve el número de elementos en la pila.
        
        Returns:
            El número de elementos en la pila.
        """
        return self.tamano_actual
    
    def vaciar(self):
        """Vacía la pila, eliminando todos sus elementos."""
        self.tope = None
        self.tamano_actual = 0
