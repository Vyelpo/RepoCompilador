import os # Para manipular archivos y directorios 
from ScriptProyect import Compilacion # Toma la clase "Compilacion" para ejecutar un archivo seleccionado
from tkinter import filedialog # Abrir un selector de archivos grafico
from pathlib import Path # cambiar rutas "c: \ .. \ .." a "c: / .. /"

class Compilador:

    def  __init__(self, rutaDir_base=filedialog.askdirectory(title="Elije la carpeta con el src")): # Elige el folder que posee el proyecto a compilar
        self.rutaBase = rutaDir_base
        pathSrc = self.BuscaSrc(rutaDir_base) # Busca el src del directorio
        if pathSrc:
            os.chdir(pathSrc)
        else:
            raise FileNotFoundError("No se encontró la carpeta 'src' en el proyecto.") # hace una excepcion en caso de que no se vea una carpeta "src" en el directorio
        
        dicJava = self.Method(pathSrc) # archivos java
        self.rutaArchivo = self.ElegirJava(dicJava)
        Compilacion(self.rutaArchivo) # llama el script de compilacion "ScriptProyect.py" para hacer funcionar el archivo seleccionado 

    def BuscaSrc(self, proyect): # Devuelve el path/direccion de la carpeta src dentro de un directorio cualquiera. Se destaca que es el primer src que encuentre en el proyecto
        for x in os.listdir(proyect):
            ruta_completa = os.path.join(proyect, x)
            if os.path.isdir(ruta_completa):
                if x == "src":
                    return ruta_completa
                else:
                    resultado = self.BuscaSrc(ruta_completa)
                    if resultado:
                        return resultado
        return None

    def Method(self, dir, dic=None): #Se apoya en recorrer_java para obtener un diccionario (archivo.java:ruta) de todos los archivos .java que se encuentren en el src
        if dic is None:
            dic = {}
        self.recorrer_java(dir, dic)
        return dic

    def recorrer_java(self, carpeta, dic):
        for x in os.listdir(carpeta):
            full_path = os.path.join(carpeta, x)
            if os.path.isdir(full_path):
                self.recorrer_java(full_path, dic)  # recursión en subcarpetas
            elif x.endswith(".java"):
                ruta_estandar = Path(full_path).as_posix()  # cambia el formato de ruta "c:\ ..\." por "c:/ .. /" por compatibilidad
                dic[x] = ruta_estandar

    def ElegirJava(self, dicc): #Metodo que en enseña todos los archivos .java que se encontro en la carpeta src
        print("El diccionario de archivos es: ")
        for x in dicc: print(x)
        clase = input("\nElija por favor el archivo java que desea compilar.\nEj: Test.java ")
        if dicc[clase]:
            print("Formato de ruta: ", dicc[clase])
            return dicc[clase]
        else:
            print("El directorio src no tiene una clase llamada: " ,dicc[clase])

#Ejemplo de uso
#Compilador()
