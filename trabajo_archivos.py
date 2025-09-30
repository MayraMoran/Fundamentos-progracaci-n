# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Mayra Morán
# Asignatura: Fundamentos de Programación
# Objetivo: Practicar operaciones básicas de escritura, lectura y cierre de archivos en Python

# --- 1. Escritura de Archivo de Texto ---
# Abrimos (o creamos) un archivo llamado "my_notes.txt" en modo escritura ("w")
# Si el archivo ya existe, su contenido será sobrescrito.
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales en el archivo
archivo.write("Primera nota: Hoy estoy aprendiendo Python.\n")
archivo.write("Segunda nota: Los archivos de texto son muy útiles.\n")
archivo.write("Tercera nota: Siempre debo cerrar los archivos después de usarlos.\n")

# Cerramos el archivo para guardar los cambios
archivo.close()

# --- 2. Lectura de Archivo de Texto ---
# Abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

# Leemos línea por línea usando readline()
print("Contenido del archivo my_notes.txt:\n")
linea = archivo.readline()
while linea:
    print(linea.strip())  # strip() elimina saltos de línea extras
    linea = archivo.readline()

# --- 3. Cierre del Archivo ---
# Cerramos el archivo después de la lectura
archivo.close()
