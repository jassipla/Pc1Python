# Leer un entero positivo N introducido por el usuario
N = int(input("Introduce un número entero positivo: "))

# Verificar si el número ingresado es positivo
if N <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Calcular la suma de los N primeros enteros positivos
    suma = (N * (N + 1)) // 2

    # Mostrar la suma de los N primeros enteros positivos
    print("La suma de los enteros desde 1 hasta", N, "es:", suma)