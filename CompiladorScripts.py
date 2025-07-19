import subprocess
import os
import sys
from tkinter import filedialog


class Compilacion:
    def __init__(self):
        self.ruta = self.pedirRuta()
        self.nombreClase = self.NombreClase(self.ruta)
        self.direct = os.path.dirname(self.ruta)
        os.chdir(os.path.dirname(self.ruta))
        compilacion = subprocess.run(
            ["javac",self.nombreClase+".java"],
            cwd=self.direct,
            capture_output=True,
            text=True
        )

        if compilacion.returncode == 0:
            print("Se cumplio la compilacion")
            ejecucion = subprocess.run(
                ["java",self.ruta],
                cwd=self.direct,
                capture_output=True,
                text=True
            )
            print("Res:\n", ejecucion.stdout)
            self.RtempFiles()
        else:
            print("Error en la compilacion:\n ", compilacion.stderr)

        

    def RtempFiles(self):
        for x in os.listdir():
            if x.endswith(".class"):
                os.remove(os.path.join(os.getcwd(),x))

    def NombreClase(self, ruta):
        return os.path.splitext(os.path.basename(self.ruta))[0]


    def pedirRuta(self):
        ret = filedialog.askopenfilename(title="Selecciona el .java")
        aux = os.path.splitext(ret)[1]
        if aux.endswith(".java"):
            return ret
        else:
            print("Elegiste un archivo de extension diferente")
            sys.exit(0)

invocacion = Compilacion()