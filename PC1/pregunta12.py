# Definir el diccionario de extensiones a tipos MIME
extensiones_a_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo
extension = nombre_archivo.lower().split('.')[-1]

# Determinar el tipo MIME correspondiente
tipo_mime = extensiones_a_mime.get("." + extension, "application/octet-stream")

# Imprimir el tipo MIME
print("Tipo MIME del archivo:", tipo_mime)