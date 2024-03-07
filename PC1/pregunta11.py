# Definir la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1, 6, 6, 7, 8, 8, 8, 9]

# Convertir la lista a un conjunto para eliminar duplicados y luego volver a convertir a lista
lista_procesada = list(set(lista_original))

# Imprimir la lista procesada
print("Lista procesada:", lista_procesada)
