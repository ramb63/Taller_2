#Promedio de N números Pide un entero N y luego N números. Calcula y muestra su promedio. (Usa un acumulador.)
N = 10
acum = 0
for _ in range(N):
    x = float(input("Ingresa el números a promediar: "))
    acum = acum + x
    prom = acum / N
    print(f"El promedio es: {prom}")