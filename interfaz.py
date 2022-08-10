from tkinter import *
from tkinter import ttk

#Clase menu principal
class Menu:
    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Práctica 1") #Titulo de la ventana
        self.ventana.resizable(False, False) #Editable
        self.ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(self.ventana, 550, 250)
        self.crearObjetos()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):
        #Frame
        self.frame1 = Frame(
            bg="#4F4E4E", 
            width="550", 
            height="250", 
            bd=20, 
            relief="groove", 
            cursor="spider").pack()

        #Labels
        Label(self.frame1, text="Curso: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=25)
        Label(self.frame1, text="Lab. Lenguajes Formales y de Programación", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=95, y=25)

        Label(self.frame1, text="Nombre del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=60)
        Label(self.frame1, text="Anthony Samuel Zea Herrera", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=235, y=60)

        Label(self.frame1, text="Carné del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=95)
        Label(self.frame1, text="202104782", bg="#4F4E4E", fg="White", font=("Centaur", 15)).place(x=215, y=95)

        #Buttons
        self.botonCargar = Button(
            self.frame1, 
            text="Cargar Archivo",
            font=("Centaur", 11, "bold"),
            command = self.ventanaCargar
            ).place(x=30, y=150)

        self.botonCursos = Button(
            self.frame1, 
            text="Gestionar cursos",
            font=("Centaur", 11, "bold"),
            command = self.ventanaGestionar
            ).place(x=170, y=150)

        self.botonCreditos = Button(
            self.frame1, 
            text="Conteo de Créditos",
            font=("Centaur", 11, "bold")
            ).place(x=315, y=150)

        self.botonSalir = Button(
            self.frame1, 
            text="Salir",
            command = self.salir,
            font=("Centaur", 11, "bold")
            ).place(x=475, y=150)

        self.ventana.mainloop()
    
    #Funciones para regresar
    def ventanaCargar(self):
        self.ventana.destroy()
        Cargar()

    def ventanaGestionar(self):
        self.ventana.destroy()
        Gestionar()
    
    def salir(self):
        self.ventana.quit()
    

#Clase cargar archivo
class Cargar:

    def __init__(self):
        self.ventana = Tk()

        #Configuracion ventana
        self.ventana.title("Cargar archivo") #Titulo de la ventana
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
        Label(self.frame, text="Ruta: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=50, y=50)

        #Caja de texto
        self.ruta = Entry(self.frame, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold")).place(x=120, y=50, width=320)

        #Buttons
        self.botonSeleccionar = Button(
            self.frame, 
            text="Seleccionar",
            font=("Centaur", 11, "bold"),
            ).place(x=250, y=100)

        self.botonRegresar = Button(
            self.frame, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command=self.ventanaMain
            ).place(x=370, y=100)

        self.ventana.mainloop()

    #Funciones para regresar
    def ventanaMain(self):
        self.ventana.destroy()
        Menu()

#Clase Gestionar cursos
class Gestionar():
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
class Listar():
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
class Agregar():
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
class Editar():
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
class Eliminar():
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
class Creditos():
    print("holamundo")

Menu()