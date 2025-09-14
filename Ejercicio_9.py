#Validación simple de nota Pide una nota entre 0 y 5. Si es inválida, 
# repite hasta que sea válida. Al final imprime la nota válida.
nota = float(input("Ingresa una nota entre 0 y 5: "))
while nota < 0 or nota > 5:
    print("Nota inválida. Intenta de nuevo.")
    nota = float(input("Ingresa una nota entre 0 y 5: "))   
print(f"La nota válida es: {nota}")