# Solicitar al usuario que ingrese cuántos shows musicales ha visto en el último año
shows_vistos = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Verificar si el usuario ha visto más de 3 shows
ha_visto_mas_de_3 = shows_vistos > 3

# Mostrar el valor de verdad
print("¿Ha visto más de 3 shows musicales en el último año?" , ha_visto_mas_de_3)