from pilas_nodos import Pila

def convertir_infija_a_postfija(expresion_infija):
    """
    Convierte una expresión aritmética en notación infija a notación postfija.
    
    Esta implementación utiliza una pila basada en nodos enlazados.
    
    Args:
        expresion_infija (str): La expresión en notación infija a convertir.
        
    Returns:
        str: La expresión convertida a notación postfija.
    """
    # Diccionario para definir la precedencia de los operadores
    precedencia = {
        '^': 3,  # Potencia (mayor precedencia)
        '*': 2,  # Multiplicación
        '/': 2,  # División
        '+': 1,  # Suma
        '-': 1   # Resta
    }
    
    # Inicializar la pila y la expresión postfija
    pila = Pila()
    expresion_postfija = ""
    
    # Procesar cada símbolo de la expresión infija
    for simbolo in expresion_infija:
        # Ignorar espacios en blanco
        if simbolo.isspace():
            continue
            
        # Si es un operando (letra o dígito), añadirlo directamente a la expresión postfija
        if simbolo.isalnum():
            expresion_postfija += simbolo
            
        # Si es un paréntesis de apertura, añadirlo a la pila
        elif simbolo == '(':
            pila.push(simbolo)
            
        # Si es un paréntesis de cierre, sacar operadores de la pila hasta encontrar el paréntesis de apertura
        elif simbolo == ')':
            while not pila.esta_vacia() and pila.peek() != '(':
                expresion_postfija += pila.pop()
                
            # Eliminar el paréntesis de apertura de la pila (si existe)
            if not pila.esta_vacia() and pila.peek() == '(':
                pila.pop()
            else:
                # Error: paréntesis desbalanceados
                return "Error: paréntesis desbalanceados"
                
        # Si es un operador
        elif simbolo in precedencia:
            # Sacar operadores de la pila mientras tengan mayor o igual precedencia
            while (not pila.esta_vacia() and 
                   pila.peek() != '(' and 
                   (pila.peek() in precedencia) and 
                   (precedencia[pila.peek()] >= precedencia[simbolo])):
                expresion_postfija += pila.pop()
                
            # Añadir el operador actual a la pila
            pila.push(simbolo)
            
        else:
            # Carácter no reconocido
            return f"Error: carácter no reconocido '{simbolo}'"
    
    # Vaciar la pila y añadir los operadores restantes a la expresión postfija
    while not pila.esta_vacia():
        if pila.peek() == '(':
            # Error: paréntesis desbalanceados
            return "Error: paréntesis desbalanceados"
        expresion_postfija += pila.pop()
    
    return expresion_postfija
