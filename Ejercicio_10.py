#Bandera de búsqueda Lee nombres (uno por línea) hasta cadena vacía. 
# Activa una bandera si aparece algún nombre que empiece por “A” (sin importar mayúsculas). 
# Al final di si se encontró o no.

Bandera = False
while True:
    nombre = input("Escriba una palabra o (espacio para salir): ".upper())
    if nombre == " ":
        break
    if nombre.upper().startswith("A"):
        Bandera = True
if Bandera:
    print("aparecio nombre con Letra A")
else:
    print("nunca aparecio nombre con Letra A")   
