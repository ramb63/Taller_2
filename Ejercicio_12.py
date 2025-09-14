#Mínimo y máximo (sentinela vacío) 
# Pide números hasta que el usuario presione ENTER vacío.
# Muestra el mínimo y el máximo ingresados. 
# Si no hubo datos, indícalo.

minimo = None
maximo = None

while True:
    Ingresos = input("Dame numeros a calcular (enter para terminar): ")
    if Ingresos == "":
        break
    n = float(Ingresos)

    if minimo is None or n < minimo:
        minimo = n
    if maximo is None or n > maximo:
        maximo = n

if minimo is None:
    print("no hubo datos.")
else:
    print(f"el mínimo ingresado: {minimo}")
    print(f"el máximo o ingresado: {maximo}")