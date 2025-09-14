#Bandera de búsqueda Lee nombres (uno por línea) hasta cadena vacía. 
# Activa una bandera si aparece algún nombre que empiece por “A” (sin importar mayúsculas). 
# Al final di si se encontró o no.

encontrado = False
while True:
    palabra = input("Escriba una palabra o espacio para salir: ")
    if palabra == " ":
        break
    if palabra == "A" or palabra == "a":
        encontrado = True
if encontrado:
    print("aparecio {a} or {A} al menos una vez")
else:
    print("nunca se escribio la palabra {a} or {A} ")   
