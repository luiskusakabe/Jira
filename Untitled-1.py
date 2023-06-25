palabra = input("Introduce una palabra: ")
numero = float(input("Introduce un número: "))
#len toma la cantidad de caracteres 
if len(palabra) == 0:
    print("No has introducido una palabra válida.")
else:
    operacion = input("Introduce una operación (+, -, *, /): ")
#operaciones
    if operacion == '+':
        resultado = len(palabra) + numero
        operacion_texto = 'sumada a'
    elif operacion == '-':
        resultado = len(palabra) - numero
        operacion_texto = 'restada a'
    elif operacion == '*':
        resultado = len(palabra) * numero
        operacion_texto = 'multiplicada por'
    elif operacion == '/':
        if numero == 0:
            print("No se puede dividir entre 0.")
            resultado = None
        else:
            resultado = len(palabra) / numero
            operacion_texto = 'dividida por'
    else:
        print("Operación no válida.")
        resultado = None

    if resultado is not None:
        print(f"La longitud de {palabra} ({len(palabra)}) ha sido {operacion_texto} {numero}: {resultado}.")
