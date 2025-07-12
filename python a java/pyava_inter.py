import subprocess
import os

# Establecemos la ruta del archivo java
rutaArchivo = r"C:\Users\20mar\OneDrive\Escritorio\Carpeta de git\random\InterfaceTest.java"
#directorio raiz del paquete (un nivel por encima de la carpeta random)
directoriobase = os.path.abspath(os.path.join(os.path.dirname(rutaArchivo),"..")) #rutaarchivo = ...\Caréta de git

# nombre completo del archivo relativo desde el directorio de la raiz
archivo_relativo = os.path.relpath(rutaArchivo, start=directoriobase)
print(archivo_relativo)

# Nombre completo de la clase (paquete.clase)
nombre_clase = "random.InterfaceTest"

# Compilar usando javac desde la raíz del paquete
compilar = subprocess.run(["javac", archivo_relativo], cwd=directoriobase, capture_output=True, text=True)


if compilar.returncode == 0:
    print("Compilación exitosa.")

    # Ejecutar la clase con su nombre completo desde la raíz del paquete
    ejecutar = subprocess.run(["java", nombre_clase], cwd=directoriobase, capture_output=True, text=True)

    print("Salida:\n", ejecutar.stdout)

else:
    print("Error al compilar:\n", compilar.stderr)    

