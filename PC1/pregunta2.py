# Solicitar el monto del consumo en el restaurante
monto_consumo = float(input("¿Cuánto fue el monto total de su consumo en el restaurante? $"))

# Solicitar el porcentaje de propina deseado
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar al mesero? (por ejemplo, 15 para el 15%) "))

# Calcular la cantidad de dinero a dejar como propina
propina = monto_consumo * (porcentaje_propina / 100)

# Mostrar la cantidad de dinero a dejar como propina
print("Debe dejar $", propina, "como propina al mesero.")