lista_numeros =[]
while True:
    nombre = input("Nombre: ")
    if nombre == "fin":
            break
    telefono = input("Número de teléfono: ")


    linea = {}
    linea["Nombre"] = nombre

    linea["Número de teléfono"] = telefono

    lista_numeros.append(linea)

print("Lista de números: \n", lista_numeros)
