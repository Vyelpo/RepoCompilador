import subprocess # Para realizar comandos en la terminal
import os # Para manipular archivos y directorios
import sys # Para cerrar el programa cuando se requiera
from tkinter import filedialog # Para llamar un selector grafico de archivos


class Compilacion:
    def __init__(self):
        self.ruta = self.pedirRuta() 
        self.nombreClase = self.NombreClase(self.ruta)
        self.direct = os.path.dirname(self.ruta) # toma el directorio del archivo cargado para ejecutar desde ahi la compilacion
        os.chdir(os.path.dirname(self.ruta))
        compilacion = subprocess.run(
            ["javac",self.nombreClase+".java"],
            cwd=self.direct,
            capture_output=True,
            text=True
        )

        if compilacion.returncode == 0: # Valida que la compilacion del archivo, es decir, en la consola sí sea un java ejecutable
            print("Se cumplio la compilacion")
            ejecucion = subprocess.run( # Realiza otra ejecucion en el cmd, pero esta vez con los .class generados para ejecutar el archivo 
                ["java",self.ruta],
                cwd=self.direct,
                capture_output=True,
                text=True
            )
            print("Res:\n", ejecucion.stdout)
            self.RtempFiles() # Elimina los .class
        else:
            print("Error en la compilacion:\n ", compilacion.stderr)

    def RtempFiles(self): # Elimina los archivos .class del directorio pertinente
        for x in os.listdir():
            if x.endswith(".class"):
                os.remove(os.path.join(os.getcwd(),x))

    def NombreClase(self, ruta): #Extrae el nombre de un archivo sin su extension
        return os.path.splitext(os.path.basename(self.ruta))[0]

    def pedirRuta(self): #Se le pide al usuario cargar un archivo .java
        ret = filedialog.askopenfilename(title="Selecciona el .java")
        aux = os.path.splitext(ret)[1]# Extrae la extension del archivo
        if aux.endswith(".java"):
            return ret
        else:
            print("Elegiste un archivo de extension diferente")
            sys.exit(0) #Termina la ejecucion del programa abrutamente

#Ejemplo de uso
#Compilacion()