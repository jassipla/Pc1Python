# Definir la lista de muestra
lista_muestra = ['Azul', 'Violeta', 'Rosado', 'Blanco', 'Morado', 'Celeste']

# Eliminar los elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]
for i in sorted(posiciones_a_eliminar, reverse=True):
    lista_muestra.pop(i)

# Imprimir la lista modificada
print(lista_muestra)