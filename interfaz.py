import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from cargar import AbrirArchivo

#Clase menu principal
class Menu(tk.Tk):
    def __init__(self):
        super().__init__()

                #Configuracion ventana
        self.title("Práctica 1") #Titulo de la ventana
        self.resizable(False, False) #Editable
        self.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self, 550, 250)
        self.crearObjetos()
        self.mainloop()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):
        #Frame
        self.frame = tk.Frame(
            bg="#4F4E4E", 
            width="550", 
            height="250", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Labels
        tk.Label(self.frame, text="Curso: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=25)
        tk.Label(self.frame, text="Lab. Lenguajes Formales y de Programación", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=95, y=25)

        tk.Label(self.frame, text="Nombre del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=60)
        tk.Label(self.frame, text="Anthony Samuel Zea Herrera", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=235, y=60)

        tk.Label(self.frame, text="Carné del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=95)
        tk.Label(self.frame, text="202104782", bg="#4F4E4E", fg="White", font=("Centaur", 15)).place(x=215, y=95)

        #Buttons
        self.botonCargar = tk.Button(
            self.frame, 
            text="Cargar Archivo",
            font=("Centaur", 11, "bold"),
            command = self.subirArchivo
            ).place(x=30, y=150)

        self.botonCursos = tk.Button(
            self.frame, 
            text="Gestionar cursos",
            font=("Centaur", 11, "bold"),
            #command = self.ventanaGestionar
            ).place(x=170, y=150)

        self.botonCreditos = tk.Button(
            self.frame, 
            text="Conteo de Créditos",
            font=("Centaur", 11, "bold"),
            #command = self.ventanaCreditos
            ).place(x=315, y=150)

        self.botonSalir = tk.Button(
            self.frame, 
            text="Salir",
            command = self.salir,
            font=("Centaur", 11, "bold")
            ).place(x=475, y=150)

    '''
    #Funciones para regresar
    def ventanaCargar(self):
        self.ventana.destroy()
        Cargar()

    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()

    def ventanaCreditos(self):
        self.ventana.destroy()
        Creditos()
    '''
    def salir(self):
        self.destroy()
        self.quit()
    
    
    ##Funcion para seleccionar un archivo
    def subirArchivo(self):
        
        #Configuracion ventana
        ventana = tk.Toplevel(self)
        ventana.title("Cargar archivo") #Titulo de la ventana
        ventana.resizable(False, False) #Editable
        ventana.iconbitmap("icono.ico") #Icono de la ventana
        ventana.configure(
            bg="#4F4E4E", 
            width="500", 
            height="200", 
            bd=20, 
            relief="groove", 
            cursor="spider")
        self.centrar(ventana, 500, 200)

        #Label
        tk.Label(ventana, text="Ruta: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=50, y=50)

        #Caja de texto
        tk.Entry(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=120, y=50, width=320)
        
        def cerrar():
            self.deiconify()
            ventana.destroy()

        def cargarFile():
            archivo = filedialog.askopenfilename()
            lista = AbrirArchivo.seleccionar(archivo)
            print(lista[0].getCodigo(), " ", lista[0].getNombre(), lista[0].getPrerequisito())
            #file = open(archivo, 'r')
            #print(file.read())
            #file.close

        #Buttons
        tk.Button(
            ventana, 
            text="Seleccionar",
            font=("Centaur", 11, "bold"),
            command=cargarFile
            ).place(x=250, y=100)

        tk.Button(
            ventana, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = cerrar
            ).place(x=370, y=100)

        #self.withdraw()

    '''
    #Funciones para regresar
    def ventanaMain(self):
        self.ventana.destroy()
        Menu()

    #Funcion para cargar
    def cargarfile(self):
        #hola = Entry.get()
        AbrirArchivo.seleccionar(hola)
    '''
'''
#Clase Gestionar cursos
class Gestionar:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Gestionar cursos") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 400, 420)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):

        #Frame
        self.frame = Frame(
            bg="#4F4E4E", 
            width="400", 
            height="420", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Buttons
        self.botonListar = Button(
            self.frame, 
            text="Listar cursos",
            font=("Centaur", 11, "bold"),
            command=self.ventanaListar,
            width=10,
            padx=20,
            pady=5
            ).place(x=140, y=50)

        self.botonAgregar = Button(
            self.frame, 
            text="Agregar Curso",
            font=("Centaur", 11, "bold"),
            command=self.ventanaAgregar,
            width=10,
            padx=20,
            pady=5
            ).place(x=140, y=120)

        self.botonEditar = Button(
            self.frame, 
            text="Editar Curso",
            font=("Centaur", 11, "bold"),
            command = self.ventanaEditar,
            width=10,
            padx=20,
            pady=5
            ).place(x=140, y=190)

        self.botonEliminar = Button(
            self.frame, 
            text="Eliminar Curso",
            font=("Centaur", 11, "bold"),
            command = self.ventanaEliminar,
            width=10,
            padx=20,
            pady=5
            ).place(x=140, y=260)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            width=10,
            padx=20,
            pady=5,
            command=self.ventanaMain
            ).place(x=140, y=330)

        self.ventana.mainloop()
    
    #Funciones para regresar
    def ventanaMain(self):
        self.ventana.destroy()
        Menu()
    
    def ventanaListar(self):
        self.ventana.destroy()
        Listar()
    
    def ventanaAgregar(self):
        self.ventana.destroy()
        Agregar()
    
    def ventanaEditar(self):
        self.ventana.destroy()
        Editar()

    def ventanaEliminar(self):
        self.ventana.destroy()
        Eliminar()

##Clase Listar cursos
class Listar:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Listar Cursos") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 1042, 500)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')
    
    def crearObjetos(self):

        #Frame para Tabla
        self.frame1 = Frame()
        self.frame1.grid(row=0, column=0)
        self.frame1.config(
            bg="#4F4E4E", 
            width="900", 
            height="500", 
            bd=20,  
            cursor="spider")

        #Frame para boton
        self.frame2 = Frame()
        self.frame2.grid(row=1, column=0)
        self.frame2.config(
            bg="#4F4E4E", 
            width="917", 
            height="80", 
            bd=20,  
            cursor="spider")
        
        #Buttons
        self.botonRegresar = Button(
            self.frame2, 
            text="Regresar",
            font=("Centaur", 18, "bold"),
            padx=20,
            pady=3,
            command=self.ventanaGestionar
            ).place(x=700, y=-10)
        
        #Tabla
        tabla = ttk.Treeview(self.frame1, columns=("#0","#1","#2", "#3", "#4", "#5"), height=15)

        tabla.grid(row=4, column=0, columnspan=2)
        tabla.column("#0", width = 125, anchor = CENTER)
        tabla.column("#1", width = 125, anchor = CENTER)
        tabla.column("#2", width = 125, anchor = CENTER)
        tabla.column("#3", width = 125, anchor = CENTER)
        tabla.column("#4", width = 125, anchor = CENTER)
        tabla.column("#5", width = 125, anchor = CENTER)
        tabla.column("#6", width = 125, anchor = CENTER)

        tabla.heading("#0", text="Código", anchor = CENTER)
        tabla.heading("#1", text="Nombre", anchor = CENTER)
        tabla.heading("#2", text="Pre Requisitos", anchor = CENTER)
        tabla.heading("#3", text="Opcionalidad", anchor = CENTER)
        tabla.heading("#4", text="Senestre", anchor = CENTER)
        tabla.heading("#5", text="Créditos", anchor = CENTER)
        tabla.heading("#6", text="Estado", anchor = CENTER)

        tabla.insert("", END, text="017", values=("Matematica", "150", "Obligatorio", "7", "4", "Cursando"))
        tabla.insert("", END, text="018", values=("Fisica 1", "103", "Obligatorio", "2", "5", "Aprobado"))

        style = ttk.Style()
        style.configure(
            "Treeview",
            background = "#BEBEBE",
            foreground = "black",
            rowheight = 25,
            fielbackground = "#BEBEBE"
        )

        style.map(
            "Treeview",
            background= [("selected", "#839192")]
        )

        self.ventana.mainloop()
    
    #Funciones para regresar
    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()

##Clase agregar curso 
class Agregar:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Agregar Curso") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 500, 450)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    
    def crearObjetos(self):

        #Frame
        self.frame = Frame(
            bg="#4F4E4E", 
            width="550", 
            height="420", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Labels
        Label(self.frame, text="Codigo: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        Label(self.frame, text="Nombre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=40, y=85)
        Label(self.frame, text="Pre requisito: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        Label(self.frame, text="Semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=40, y=185)
        Label(self.frame, text="Opcionalidad: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=235)
        Label(self.frame, text="Estado", bg="#4F4E4E", fg="White", font=("Centaur", 15)).place(x=40, y=285)

        #Cajas de texto
        self.codigo = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=35, width=320)
        self.nombre = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=85, width=320)
        self.pre_requisito = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=135, width=320)
        self.semestre = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=185, width=320)
        self.opcionalidad = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=235, width=320)
        self.estado = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=285, width=320)

        #Buttons
        self.botonAgregar = Button(
            self.frame, 
            text="Agregar",
            font=("Centaur", 11, "bold"),
            width=10,
            padx=15,
            pady=5
            ).place(x=225, y=335)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = self.ventanaGestionar,
            width=10,
            padx=15,
            pady=5
            ).place(x=373, y=335)


    #Funciones para regresar
    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()

##Clase editar curso 
class Editar:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Editar Curso") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 500, 450)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    
    def crearObjetos(self):

        #Frame
        self.frame = Frame(
            bg="#4F4E4E", 
            width="550", 
            height="420", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Labels
        Label(self.frame, text="Codigo: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        Label(self.frame, text="Nombre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=40, y=85)
        Label(self.frame, text="Pre requisito: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        Label(self.frame, text="Semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=40, y=185)
        Label(self.frame, text="Opcionalidad: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=235)
        Label(self.frame, text="Estado", bg="#4F4E4E", fg="White", font=("Centaur", 15)).place(x=40, y=285)

        #Cajas de texto
        self.codigo = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=35, width=320)
        self.nombre = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=85, width=320)
        self.pre_requisito = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=135, width=320)
        self.semestre = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=185, width=320)
        self.opcionalidad = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=235, width=320)
        self.estado = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=180, y=285, width=320)

        #Buttons
        self.botonEditar = Button(
            self.frame, 
            text="Editar",
            font=("Centaur", 11, "bold"),
            width=10,
            padx=15,
            pady=5
            ).place(x=225, y=335)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = self.ventanaGestionar,
            width=10,
            padx=15,
            pady=5
            ).place(x=373, y=335)

    #Funciones para regresar
    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()

##Clase eliminar curso
class Eliminar:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Eliminar Curso") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 500, 200)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):

        #Frame
        self.frame = Frame(
            bg="#4F4E4E", 
            width="500", 
            height="200", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Label
        Label(self.frame, text="Código de Curso: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=50, y=50)

        #Caja de texto
        self.ruta = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=210, y=50, width=230)

        #Buttons
        self.botonEliminar = Button(
            self.frame, 
            text="Eliminar",
            font=("Centaur", 11, "bold"),
            ).place(x=280, y=100)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command=self.ventanaGestionar
            ).place(x=370, y=100)


        self.ventana.mainloop()

    #Funciones para regresar
    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()

#Clase Conteo de creditos
class Creditos:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Conteo de Créditos") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 500, 450)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):

        #Frame
        self.frame = Frame(
            bg="#4F4E4E", 
            width="500", 
            height="450", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Labels
        Label(self.frame, text="Créditos aprobados: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        Label(self.frame, text="Créditos cursando: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=85)
        Label(self.frame, text="Créditos pendientes: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        Label(self.frame, text="Créditos hasta el semestre N: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=185)
        Label(self.frame, text="Créditos del semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=275)

        #Caja de texto
        self.semestre_N = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=300, y=185, width=30)
        self.semestre = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=250, y=275, width=30)

        #Buttons
        self.botonContarN = Button(
            self.frame, 
            text="Contar",
            font=("Centaur", 10, "bold"),
            width=8,
            padx=8,
            pady=5
            ).place(x=195, y=228)

        #Buttons
        self.botonContarS = Button(
            self.frame, 
            text="Contar",
            font=("Centaur", 10, "bold"),
            width=8,
            padx=8,
            pady=5
            ).place(x=195, y=320)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = self.ventanaGestionar,
            width=10,
            padx=15,
            pady=5
            ).place(x=330, y=370)
        
        self.ventana.mainloop()

    #Funciones para regresar
    def ventanaGestionar(self):
        self.ventana.destroy()
        Menu()
'''

Menu()