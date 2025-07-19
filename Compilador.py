import subprocess
import os
import sys
from tkinter import filedialog
#metodo para eliminar los .class generados por la compilacion
def EliminarArchCls():
    for x in os.listdir():
        if x.endswith(".class"):
            os.remove(os.path.join(os.getcwd(),x)) #elimina los archivos .class generados de la compilacion

#Metodo para obtener el nombre del archivo sin extension (.java)
def NombreClase(ruta):
    return os.path.splitext(os.path.basename(ruta))[0] #retorna el nombre de la clase sin el .java

#metodo para llamar la ventana de archivos del sistema y obtener el archivo a compilar
def pedirRuta():
    ruta=  filedialog.askopenfilename(title="Selecciona el .java")
    aux = os.path.splitext(ruta)[1]
    if aux.endswith(".java"):
        return ruta
    else:
        print("Elegiste un archivo de extension diferente")
        sys.exit(0)


rutaArchivo = pedirRuta() #Ruta
nombreClase = NombreClase(rutaArchivo) #Nombre de la clase
directorioArchivo = os.path.dirname(rutaArchivo)


#Nos movemos hacia el directorio en el cual esta el archivo a compilar
os.chdir(os.path.dirname(rutaArchivo)) #nos movemos hacia el directorio donde esta el archivo java
#print("directorio Archivo:", directorioArchivo, "\nDirectorio actual: ", os.getcwd())

compilacion = subprocess.run(
    ["javac", nombreClase+".java"],
    cwd=directorioArchivo,
    capture_output=True,
    text=True
)

if compilacion.returncode == 0:
    print("Se cumplio la compilacion: ")

    #se ejecuta
    ejecucion = subprocess.run(
        ["java",rutaArchivo],
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

