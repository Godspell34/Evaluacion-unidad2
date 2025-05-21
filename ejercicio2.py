"""
    Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
Use una pila para realizar el seguimiento de los paréntesis abiertos.
"""

class Nodo:
    """ Clase Nodo para la pila """
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None

class Pila:
    """ Clase Pila para almacenar caracteres """
    def __init__(self):
        self.peak = None

    def apilar(self, caracter):
        """ Apila un caracter en la pila """
        nuevo_nodo = Nodo(caracter)
        nuevo_nodo.siguiente = self.peak
        self.peak = nuevo_nodo

    def desapilar(self):
        """ Desapila un caracter de la pila """
        if self.peak is None:
            return None
        caracter = self.peak.caracter
        self.peak = self.peak.siguiente
        return caracter

    def es_vacia(self):
        """ Verifica si la pila está vacía """
        return self.peak is None
    
    def verificar_balanceados(cadena):
        """ Verifica si los paréntesis en la cadena están balanceados """
        pila = Pila()
        pares = {')': '(', '}': '{', ']': '['}

        for caracter in cadena:
            if caracter in pares.values():
                # Si es un paréntesis abierto, apilarlo
                pila.apilar(caracter)
            elif caracter in pares.keys():
                # Si es un paréntesis cerrado, verificar si coincide con el último abierto
                if pila.es_vacia() or pila.desapilar() != pares[caracter]:
                    return False
        # Si la pila está vacía al final, todos los paréntesis están balanceados
        return pila.es_vacia()

# Ejemplo de uso
frase = "print(f\"Hola mundo desde {uam}\")"
print("Cadena original:", frase)

if Pila.verificar_balanceados(frase):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
