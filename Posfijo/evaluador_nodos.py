from pilas_nodos import Pila

def evaluar_expresion_postfija(expresion_postfija):
    """
    Evalúa una expresión aritmética en notación postfija.
    
    Esta implementación utiliza una pila basada en nodos enlazados.
    
    Args:
        expresion_postfija (str): La expresión en notación postfija a evaluar.
        
    Returns:
        float: El resultado de la evaluación de la expresión.
        
    Raises:
        ValueError: Si la expresión no es válida o contiene operadores no soportados.
    """
    pila = Pila()
    
    # Procesar cada símbolo de la expresión postfija
    for simbolo in expresion_postfija:
        # Ignorar espacios en blanco
        if simbolo.isspace():
            continue
            
        # Si es un operando (dígito), convertirlo a número y añadirlo a la pila
        if simbolo.isdigit():
            pila.push(int(simbolo))
            
        # Si es un operador, sacar dos operandos de la pila, realizar la operación y añadir el resultado
        elif simbolo in "+-*/^":
            # Verificar que haya al menos dos operandos en la pila
            if pila.tamano() < 2:
                raise ValueError("Expresión postfija inválida: faltan operandos")
                
            # Sacar los operandos (el segundo operando sale primero)
            operando2 = pila.pop()
            operando1 = pila.pop()
            
            # Realizar la operación correspondiente
            if simbolo == '+':
                pila.push(operando1 + operando2)
            elif simbolo == '-':
                pila.push(operando1 - operando2)
            elif simbolo == '*':
                pila.push(operando1 * operando2)
            elif simbolo == '/':
                # Verificar división por cero
                if operando2 == 0:
                    raise ValueError("Error: División por cero")
                pila.push(operando1 / operando2)
            elif simbolo == '^':
                pila.push(operando1 ** operando2)
        else:
            # Carácter no reconocido
            raise ValueError(f"Error: carácter no reconocido '{simbolo}'")
    
    # Al final, la pila debe contener exactamente un elemento (el resultado)
    if pila.tamano() != 1:
        raise ValueError("Expresión postfija inválida: sobran operandos")
        
    return pila.pop()
