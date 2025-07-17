import subprocess
import os

#metodo para eliminar los .class generados por la compilacion
def EliminarArchCls():
    for x in os.listdir():
        if x.endswith(".class"):
            os.remove(os.path.join(os.getcwd(),x)) #elimina los archivos .class generados de la compilacion

def NombreClase(ruta):
    return os.path.splitext(os.path.basename(ruta))[0] #retorna el nombre de la clase sin el .java

rutaArchivo = r"C:\Users\20mar\OneDrive\Escritorio\Carpeta de git\Interfaz.java" #Ruta
nombreClase = NombreClase(rutaArchivo) #Nombre de la clase
directorioArchivo = os.path.dirname(rutaArchivo)
os.chdir(os.path.dirname(rutaArchivo)) #nos movemos hacia el directorio donde esta el archivo java
print("directorio Archivo:", directorioArchivo, "\nDirectorio actual: ", os.getcwd())

compilacion = subprocess.run(
    ["javac",nombreClase+".java"],
    cwd=os.path.dirname(rutaArchivo),
    capture_output=True,
    text=True
)

if compilacion.returncode == 0:
    print("Se cumplio la compilacion: ")

    #se ejecuta
    ejecucion = subprocess.run(
        ["java",nombreClase],
        cwd=os.path.dirname(rutaArchivo),
        capture_output=True,
        text=True
    )

    print("Salida:\n", ejecucion.stdout,"\n Errores: \n",ejecucion.stderr) #si errores no muestra nada signfica que todo fue bien, logico pero no obvio en este caso


    print("Eliminando archivo extra..")
    EliminarArchCls()

else:
    print("Err:\n", compilacion.stderr)
    
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, 
# capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, 
# errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)

