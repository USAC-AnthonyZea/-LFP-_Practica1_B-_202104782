from tkinter import messagebox
import os

#Encapsulamiento
class Cursos():

    #Constructor
    def __init__(self, codigo, nombre, prerequisto, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisito = prerequisto
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    #Getters
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrerequisito(self):
        return self.prerequisito

    def getObligatorio(self):
        if self.obligatorio == "1":
            return "Obligatorio"
        elif self.obligatorio == "0":
            return "Opcional"

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos

    def getEstado(self):
        if self.estado == "0\n" or self.estado == "0":
            return "Aprobado"
        elif self.estado == "1\n" or self.estado == "1":
            return "Cursando"
        elif self.estado == "-1\n" or self.estado == "-1":
            return "Pendiente"

    #Setters
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrerequisito(self, prerequisito):
        self.prerequisito = prerequisito

    def setObligatorio(self,obligatorio):
        self.obligatorio = obligatorio
        
    def setSemestre(self, semestre):
        self.semestre = semestre

    def setCreditos(self, creditos):
        self.creditos = creditos

    def setEstado(self, estado):
        self.estado = estado

#Clase para abrir el archivo y leer su contenido
class AbrirArchivo():
        
    def seleccionar(archivo):

        ruta, extension = os.path.splitext(archivo)

        if extension == ".LFP" or extension == ".lfp":

            print(ruta + "\n")
            print("Archivo cargado con exito")
            fileOpen = open(archivo, "r+", encoding="utf-8") #Lo abrimos
            lineas = fileOpen.readlines() #Leemos su contenido
            fileOpen.close() #Cerramos el archivo

            print(lineas)

            lista = [] #Creamos lista para almacenar los datos de los cursos

            for linea in lineas:
            
                data = linea.split(',') #Devuelve una lista
                print(data)
                curso = Cursos(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                lista.append(curso)
                
            return lista
        
        else:
            messagebox.showerror(message="La extension del archivo no es '.LFP'", title="Error")

