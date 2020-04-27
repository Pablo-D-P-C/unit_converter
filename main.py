while True:
    print("Bienvenidos al convertidor de Kilometros a Milla!")

    km = float(input("Introduce el número de Kilometros: "))
    millas = km * 0.621371192
    print("El resultado de la conversión es: ",millas)
    print("Quieres convertir otra unidad? Si ó No.")
    respuesta = input()
    if respuesta == "Si" or respuesta == "si":
        print()
    elif respuesta == "No" or respuesta == "no":
        print("Saliendo del convertidor de unidades ..........")
        break
    else:
        print("No se reconoce este comando.")