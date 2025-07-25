import subprocess
import os
import sys

class Compilacion:
    def __init__(self, ruta):
        self.ruta = ruta
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
    
# Este programa tiene la misma logica que el compilador de scripts (CompiladorScripts.py).
# La unica excepcion o diferencia que tiene es que la ruta que recibe no tiene que buscarla
# el usuario, sino que se ingresa como argumento en la clase que posee el compilador. Razon la cual
# no tiene el metodo "Pedir ruta" como sucede en el otro programa ya mencionado
