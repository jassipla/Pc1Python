# Solicitar la edad del cliente al usuario
edad_cliente = int(input("Por favor, ingrese su edad: "))

# Calcular el precio de la entrada basado en la edad
if edad_cliente < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif edad_cliente <= 18:
    precio_entrada = 5  # Clientes de 4 a 18 años pagan $5
else:
    precio_entrada = 10  # Clientes mayores de 18 años pagan $10

# Mostrar el precio de la entrada al cliente
print("El precio de la entrada es: $" + str(precio_entrada))