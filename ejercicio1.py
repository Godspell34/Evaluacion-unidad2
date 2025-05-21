""" Ejercicio #1: Inversión de palabras en una frase. Desarrolle un programa que
utilice una pila para invertir el orden de las palabras en una frase dada. Por ejemplo,
la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola". """

class Nodo:
    """ Clase Nodo para la pila """
    def __init__(self, palabra):
        self.palabra = palabra
        self.siguiente = None

class Pila:
    """ Clase Pila para almacenar palabras """
    def __init__(self):
        self.peak = None

    def apilar(self, palabra):
        """ Apila una palabra en la pila """
        nuevo_nodo = Nodo(palabra)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def desapilar(self):
        """ Desapila una palabra de la pila """
        if self.cima is None:
            return None
        palabra = self.cima.palabra
        self.cima = self.cima.siguiente
        return palabra

    def es_vacia(self):
        """ Verifica si la pila está vacía """
        return self.cima is None
    
    def invertir_frase(frase):
        """ Invierte el orden de las palabras en una frase """
        pila = Pila()
        palabras = frase.split()

        # Apilar cada palabra en la pila
        for palabra in palabras:
            pila.apilar(palabra)

        # Desapilar las palabras para invertir el orden
        frase_invertida = []
        while not pila.es_vacia():
            frase_invertida.append(pila.desapilar())

        return ' '.join(frase_invertida)
    
# Ejemplo de uso
if __name__ == "__main__":
    frase = "Hola mundo desde UAM"
    print("Frase original:", frase)
    frase_invertida = Pila.invertir_frase(frase)
    print("Frase invertida:", frase_invertida)
    
