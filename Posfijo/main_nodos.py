import sys
from pilas_nodos import Pila
from conversor_nodos import convertir_infija_a_postfija
from evaluador_nodos import evaluar_expresion_postfija

def main():
    """
    Programa principal para probar la conversión y evaluación de expresiones aritméticas
    utilizando una implementación de pila basada en nodos enlazados.
    """
    print("PROGRAMA DE CONVERSIÓN Y EVALUACIÓN DE EXPRESIONES ARITMÉTICAS")
    print("(Implementación con pilas basadas en nodos enlazados)")
    print("=" * 70)
    
    # Ejemplos de conversión de infija a postfija del PDF
    ejemplos_conversion = [
        "X+Z*W",
        "(X+Z)*W/T^Y-V",
        "A+B*C",
        "A+B-C",
        "X^Y*W",
        "A-B*C/D",
        "A+B*(A+B*C)",
        "(A+B)*E+F",
        "(A+B)*(C-D)^E*F",
        "(A+B)*(C^(D-E)+F)-G",
        "M*P+(A/B+C)",
        "A*(B+C)*(C+B-A)"
    ]
    
    print("\nEJEMPLOS DE CONVERSIÓN DE INFIJA A POSTFIJA:")
    print("-" * 70)
    for i, ejemplo in enumerate(ejemplos_conversion, 1):
        resultado = convertir_infija_a_postfija(ejemplo)
        print(f"{i}. Infija: {ejemplo}")
        print(f"   Postfija: {resultado}")
        print()
    
    # Ejemplos de evaluación de expresiones del PDF
    ejemplos_evaluacion = [
        ("6+4*(9+5*2-3)", "64952*+3-*+"),
        ("5*4+(9/3+8*2)", "54*93/82*++"),
        ("7+3*(9+5*2^3-8)", "73952^*+8-*+"),
        ("4*(2+3-2)*(4+8-5)", "423+2-*48+5-*"),
        ("8+4+((5^2+6)*4)", "84+52^6+4*+"),
        ("6*2+8-3*2/2", "62*8+32*2/+")
    ]
    
    print("\nEJEMPLOS DE EVALUACIÓN DE EXPRESIONES POSTFIJAS:")
    print("-" * 70)
    for i, (infija, postfija) in enumerate(ejemplos_evaluacion, 1):
        try:
            # Verificar que nuestra conversión coincide con la postfija esperada
            nuestra_postfija = convertir_infija_a_postfija(infija.replace(" ", ""))
            print(f"{i}. Infija: {infija}")
            print(f"   Postfija esperada: {postfija}")
            print(f"   Nuestra conversión: {nuestra_postfija}")
            
            # Para la evaluación, usaremos solo expresiones con dígitos simples como se indica en el PDF
            if all(c.isdigit() or c in "+-*/^" for c in postfija):
                resultado = evaluar_expresion_postfija(postfija)
                print(f"   Resultado de la evaluación: {resultado}")
            else:
                print("   (No se puede evaluar: contiene variables)")
        except Exception as e:
            print(f"   Error: {e}")
        print()
    
    # Modo interactivo
    print("\nMODO INTERACTIVO:")
    print("-" * 70)
    print("Ingrese una expresión aritmética en notación infija (o 'salir' para terminar):")
    
    while True:
        expresion = input("> ")
        if expresion.lower() == 'salir':
            break
            
        try:
            # Convertir a postfija
            postfija = convertir_infija_a_postfija(expresion.replace(" ", ""))
            print(f"Expresión postfija: {postfija}")
            
            # Evaluar si solo contiene dígitos y operadores
            if all(c.isdigit() or c in "+-*/^" for c in postfija):
                resultado = evaluar_expresion_postfija(postfija)
                print(f"Resultado: {resultado}")
            else:
                print("No se puede evaluar: la expresión contiene variables.")
        except Exception as e:
            print(f"Error: {e}")
        print()

if __name__ == "__main__":
    main()
