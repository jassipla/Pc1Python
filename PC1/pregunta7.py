# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta de los dos números (primer número menos segundo número)")
    print("3. Mostrar multiplicación de los dos números")
    opcion = input("Opción: ")
    return opcion

# Leer dos números por teclado
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú y obtener la opción del usuario
opcion = mostrar_menu()

# Realizar la operación correspondiente según la opción elegida
if opcion == "1":
    resultado = numero1 + numero2
    print("La suma de", numero1, "y", numero2, "es:", resultado)
elif opcion == "2":
    resultado = numero1 - numero2
    print("La resta de", numero1, "y", numero2, "es:", resultado)
elif opcion == "3":
    resultado = numero1 * numero2
    print("La multiplicación de", numero1, "y", numero2, "es:", resultado)
else:
    print("Opción no válida. Por favor, seleccione una opción válida (1, 2 o 3).")