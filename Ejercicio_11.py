# """ Menú básico (while True + break) 
# Menú: 1) Sumar al total 2) Ver total 0) Salir.
# Opción 1: pide un número y lo suma al total.
# Opción 2: muestra el total actual.
# Opción 0: sale del menú con break. """

total = 0.0


while True:
    print("\n  Menú básico:")
    print("1) Sumar al total")
    print("2) Ver total")
    print("0) Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        n = int(input("ingrese un valor a sumar: "))
        total == n
        if n == 0:
            break
        if n < 0:
            continue
        total = total + n
        
        
    elif opcion == "2":
        print(f"Total actual: {total:}")
        
    elif opcion == "0":
        print("sale del menú")
        break
    
    else:
        print("Opción no válida")
