# Solicitar al usuario la hora en formato HH:MM
hora_usuario = input("Por favor, ingrese la hora en formato HH:MM: ")

# Separar la hora y los minutos
hora, minutos = map(int, hora_usuario.split(':'))

# Convertir la hora y los minutos a un único número decimal
hora_decimal = hora + minutos / 60

# Verificar si es hora de desayunar, almorzar o cenar
if 7 <= hora_decimal <= 8:
    print("Es hora de desayunar.")
elif 12 <= hora_decimal <= 13:
    print("Es hora de almorzar.")
elif 18 <= hora_decimal <= 19:
    print("Es hora de cenar.")