#Suma hasta 0 (sentinela) Pide montos (decimales). Termina cuando ingresen 0. Muestra cantidad de montos y total.

suma, conteo = 0 , 0
while True:
    monto = float(input("Monto (0 para terminar): "))
    if monto == 0:
        break
    monto =float(monto)
    suma = suma + monto
    conteo = conteo + 1
    print(f"Cantidad de montos: {conteo},Total: {suma}")