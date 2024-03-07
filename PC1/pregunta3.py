# Definir el peso de los payasos y muñecas en gramos
peso_payaso = 112
peso_muñeca = 75

# Solicitar al usuario el número de payasos vendidos
num_payasos = int(input("Ingrese el número de payasos vendidos: "))

# Solicitar al usuario el número de muñecas vendidas
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total_paquete = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)

# Mostrar el peso total del paquete
print("El peso total del paquete que será enviado es:", peso_total_paquete, "gramos.")