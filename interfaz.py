import tkinter as tk
from tkinter import END, filedialog
from tkinter import ttk
from cargar import AbrirArchivo
from cargar import Cursos
from tkinter import messagebox

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

        # Lista global
        self.list_global = []

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)

        r.geometry(f'+{x}+{y}')

    def crearObjetos(self):
        
        #Configuracion ventana
        self.configure(bg="#4F4E4E", 
            width="550", 
            height="250", 
            bd=20, 
            relief="groove", 
            cursor="spider")

        #Labels
        tk.Label(self, text="Curso: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=25)
        tk.Label(self, text="Lab. Lenguajes Formales y de Programación", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=95, y=25)

        tk.Label(self, text="Nombre del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=60)
        tk.Label(self, text="Anthony Samuel Zea Herrera", fg="White", bg="#4F4E4E", font=("Centaur", 15)).place(x=235, y=60)

        tk.Label(self, text="Carné del estudiante: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=30, y=95)
        tk.Label(self, text="202104782", bg="#4F4E4E", fg="White", font=("Centaur", 15)).place(x=215, y=95)

        #Buttons
        botonCargar = tk.Button(
            self, 
            text="Cargar Archivo",
            font=("Centaur", 11, "bold"),
            command = self.opcionesCargar
            ).place(x=20, y=150)

        botonCursos = tk.Button(
            self, 
            text="Gestionar cursos",
            font=("Centaur", 11, "bold"),
            command = self.opcionesGestionar
            #command = self.ventanaGestionar
            ).place(x=150, y=150)

        botonCreditos = tk.Button(
            self, 
            text="Conteo de Créditos",
            font=("Centaur", 11, "bold"),
            command = self.opcionesCreditos
            ).place(x=287, y=150)

        botonSalir = tk.Button(
            self, 
            text="Salir",
            command = lambda: self.quit(),
            font=("Centaur", 11, "bold")
            ).place(x=440, y=150)

    #### Funciones para abrir y cerrar ventanas
    def opcionesCargar(self):

        self.withdraw() 
        self.subirArchivo()
    
    def opcionesGestionar(self):

        self.withdraw() 
        self.gestionarCursos()
    
    def opcionesCreditos(self):

        self.withdraw() 
        self.conteoCreditos()
          
    
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
        labelRuta = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelRuta.place(x=120, y=50, width=320)
        
        ### Funcion cerrar ventana
        def cerrar():
            self.deiconify()
            ventana.destroy()
            
        ### Funcion seleccionador de archivo
        def cargarFile():

            varRuta = tk.StringVar()

            try:
                archivo = filedialog.askopenfilename()
                lista = AbrirArchivo.seleccionar(archivo)
                varRuta.set(archivo)

                labelRuta.config(textvariable=varRuta)
                
                ##Agregando todos los elementos en la lista extra
                for i in lista:
                    self.list_global.append(i)

            except TypeError:
                print("No se puede imprimir nada")

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

    ##Funcion para gestionar cursos
    def gestionarCursos(self):

        #Configuracion ventana
        ventana = tk.Toplevel(self)
        ventana.title("Gestionar cursos") #Titulo de la ventana
        ventana.resizable(False, False) #Editable
        ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventana, 400, 420)
        ventana.configure(
            bg="#4F4E4E", 
            width="400", 
            height="480", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )
        
        ### Funcion abrir y cerrar ventana listar cursos
        def ventanaListar():
            ventana.destroy()
            self.listarCursos()

        #Buttons
        botonListar = tk.Button(
            ventana, 
            text="Listar cursos",
            font=("Centaur", 11, "bold"),
            command=ventanaListar,
            width=10,
            padx=20,
            pady=5
            ).place(x=120, y=30)

        ### Funcion abrir y cerrar ventana mostrar cursos
        def ventanaMostrar():
           ventana.destroy()
           self.mostrarCurso()

        botonMostrar = tk.Button(
            ventana, 
            text="Mostrar curso",
            font=("Centaur", 11, "bold"),
            command=ventanaMostrar,
            width=10,
            padx=20,
            pady=5
            ).place(x=120, y=100)

        ### Funcion abrir y cerrar ventana agregar cursos
        def ventanaAgregar():
            ventana.destroy()
            self.agregarCurso()

        botonAgregar = tk.Button(
            ventana, 
            text="Agregar Curso",
            font=("Centaur", 11, "bold"),
            command=ventanaAgregar,
            width=10,
            padx=20,
            pady=5
            ).place(x=120, y=170)

        ### Funcion abrir y cerrar ventana editar cursos
        def ventanaEditar():
            ventana.destroy()
            self.editarCurso()

        botonEditar = tk.Button(
            ventana, 
            text="Editar Curso",
            font=("Centaur", 11, "bold"),
            command = ventanaEditar,
            width=10,
            padx=20,
            pady=5
            ).place(x=120, y=240)

        ### Funcion abrir y cerrar ventana editar cursos
        def ventanaEliminar():
            ventana.destroy()
            self.eliminarCurso()

        botonEliminar = tk.Button(
            ventana, 
            text="Eliminar Curso",
            font=("Centaur", 11, "bold"),
            command = ventanaEliminar,
            width=10,
            padx=20,
            pady=5
            ).place(x=120, y=310)

        def cerrar():
            self.deiconify()
            ventana.destroy()

        botonRegresar = tk.Button(
            ventana, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            width=10,
            padx=20,
            pady=5,
            command=cerrar
            ).place(x=120, y=380)

    ### Funcion para listar los cursos
    def listarCursos(self):

        #Configuracion ventana
        ventanaL = tk.Toplevel(self)
        ventanaL.title("Listar Cursos") #Titulo de la ventana
        ventanaL.resizable(False, False) #Editable
        ventanaL.iconbitmap("icono.ico") #Icono de la ventana
        ventanaL.configure(
            bg="#4F4E4E", 
            bd=20,
            relief="groove",
            cursor="spider")
        self.centrar(ventanaL, 1042, 500)
        
        def regresar():
            ventanaL.withdraw()
            self.gestionarCursos()

        #Buttons
        botonRegresar = tk.Button(
            ventanaL, 
            text="Regresar",
            font=("Centaur", 18, "bold"),
            command = regresar
            )
        botonRegresar.grid(row=5, column=3)
        
        #Tabla
        column = ("Codigo", "Nombre", "Pre Requisito", "Opcionalidad", "Semestre", "Creditos", "Estado")

        tabla = ttk.Treeview(ventanaL, columns = column, show="headings")
        tabla.grid(row=1, column=1)

        # Creando columnas
        tabla.heading("Codigo", text="Código")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Pre Requisito", text="Pre Requisitos")
        tabla.heading("Opcionalidad", text="Opcionalidad")
        tabla.heading("Semestre", text="Semestre")
        tabla.heading("Creditos", text="Créditos")
        tabla.heading("Estado", text="Estado")

        _curso = [] # lista temporal

        #Agregando valores a la tabla
        for i in range(len(self.list_global)):

            valores = (self.list_global[i].getCodigo(), self.list_global[i].getNombre(), self.list_global[i].getPrerequisito(), self.list_global[i].getObligatorio(), self.list_global[i].getSemestre(), self.list_global[i].getCreditos(), self.list_global[i].getEstado())
            _curso.append(valores)

        # Agregando valores a la tabla
        for x in _curso:
            tabla.insert("", tk.END, values = x)
    
        #Estilo tabla
        style = ttk.Style()
        style.configure(
            "Treeview",
            background = "#BEBEBE",
            foreground = "black",
            rowheight = 30,
            fielbackground = "#BEBEBE"
        )
#        #Mapeo y seleccion de tabla
        style.map(
            "Treeview",
            background= [("selected", "#839192")]
        )
    
    ### Funcion para mostrar cursos
    def mostrarCurso(self):

        #Configuracion ventana
        ventanaM = tk.Toplevel(self)
        ventanaM.title("Mostrar Curso") #Titulo de la ventana
        ventanaM.resizable(False, False) #Editable
        ventanaM.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventanaM, 550, 500)
        ventanaM.configure(
            bg="#4F4E4E", 
            width="550", 
            height="500", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )

        #Labels
        tk.Label(ventanaM, text="Codigo: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        tk.Label(ventanaM, text="Nombre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=85)
        tk.Label(ventanaM, text="Pre requisito: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        tk.Label(ventanaM, text="Semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=185)
        tk.Label(ventanaM, text="Opcionalidad: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=235)
        tk.Label(ventanaM, text="Creditos: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=285)
        tk.Label(ventanaM, text="Estado:", bg="#4F4E4E", fg="White", font=("Centaur", 15, "bold")).place(x=40, y=335)

        #Widgets para mostrar dtos
        textCodigo = tk.Entry(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelNombre = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelPre_requisito = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelSemestre = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelOpcionalidad = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelCreditos = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelEstado = tk.Label(ventanaM, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))

        ##Posicion widgets
        textCodigo.place(x=180, y=35, width=320)

        labelNombre.place(x=180, y=85, width=320)
        labelPre_requisito.place(x=180, y=135, width=320)
        labelSemestre.place(x=180, y=185, width=320)
        labelOpcionalidad.place(x=180, y=235, width=320)
        labelCreditos.place(x=180, y=285, width=320)
        labelEstado.place(x=180, y=335, width=320) 

        ##Funcion para buscar el curso
        def viewCurso():

            temporal = False

            for i in range(len(self.list_global)):

                if textCodigo.get() == self.list_global[i].getCodigo():

                    #Variables de texto
                    _name = tk.StringVar()
                    _prerequisito = tk.StringVar()
                    _semestre = tk.StringVar()
                    _opcionalidad = tk.StringVar()
                    _creditos = tk.StringVar()
                    _estado = tk.StringVar()

                    _name.set(self.list_global[i].getNombre())
                    _prerequisito.set(self.list_global[i].getPrerequisito())
                    _semestre.set(self.list_global[i].getSemestre())
                    _opcionalidad.set(self.list_global[i].getObligatorio())                        
                    _creditos.set(self.list_global[i].getCreditos())
                    _estado.set(self.list_global[i].getEstado())

                    labelNombre.config(textvariable = _name)
                    labelPre_requisito.config(textvariable = _prerequisito)
                    labelSemestre.config(textvariable = _semestre)
                    labelOpcionalidad.config(textvariable = _opcionalidad)
                    labelCreditos.config(textvariable = _creditos)
                    labelEstado.config(textvariable = _estado)

                    temporal = True

            if temporal == False:
                messagebox.showinfo(message="El curso no existe", title="Codigo incorrecto")

        #Buttons
        botonMostrar = tk.Button(
            ventanaM, 
            text="Mostrar",
            font=("Centaur", 11, "bold"),
            command = viewCurso,
            width=10,
            padx=15,
            pady=5
            ).place(x=225, y=400)
        
        def regresar():
            ventanaM.withdraw()
            self.gestionarCursos()

        botonRegresar = tk.Button(
            ventanaM, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = regresar,
            width=10,
            padx=15,
            pady=5
            ).place(x=373, y=400)

    ### Funcion para agregar cursos
    def agregarCurso(self):

        #Configuracion ventana
        ventanaA = tk.Toplevel(self)
        ventanaA.title("Agregar Curso") #Titulo de la ventana
        ventanaA.resizable(False, False) #Editable
        ventanaA.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventanaA, 550, 500)
        ventanaA.configure(
            bg="#4F4E4E", 
            width="550", 
            height="500", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )

        #Labels
        tk.Label(ventanaA, text="Codigo: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        tk.Label(ventanaA, text="Nombre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=85)
        tk.Label(ventanaA, text="Pre requisito: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        tk.Label(ventanaA, text="Semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=185)
        tk.Label(ventanaA, text="Opcionalidad: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=235)
        tk.Label(ventanaA, text="Creditos: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=285)
        tk.Label(ventanaA, text="Estado:", bg="#4F4E4E", fg="White", font=("Centaur", 15, "bold")).place(x=40, y=335)

        #Cajas de texto
        textCodigo = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        textNombre = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        textPre_requisito = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        textSemestre = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))#.place(x=180, y=185, width=320)
        textOpcionalidad = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))#.place(x=180, y=235, width=320)
        textCreditos = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))#.place(x=180, y=235, width=320)
        textEstado = tk.Entry(ventanaA, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))#.place(x=180, y=285, width=320)

        ##Posicion cajas de texto
        textCodigo.place(x=180, y=35, width=320)
        textNombre.place(x=180, y=85, width=320)
        textPre_requisito.place(x=180, y=135, width=320)
        textSemestre.place(x=180, y=185, width=320)
        textOpcionalidad.place(x=180, y=235, width=320)
        textCreditos.place(x=180, y=285, width=320)
        textEstado.place(x=180, y=335, width=320)

        ## Funcion para añadir cursos en la tabla
        def addCurso():
            condicional = False
            for i in range(len(self.list_global)):
                if textCodigo.get() == self.list_global[i].getCodigo():  
                    condicional = True
                    break

            if condicional == True:
                messagebox.showinfo(message = "El curso ya se encuentre en el sistema", title = "Curso añadido")

            else:
                if (textOpcionalidad.get() != "1" and textOpcionalidad.get() != "0" or textEstado.get() != "0" and textEstado.get() != "1" and textEstado.get() != "-1") or (int(textCreditos.get()) < 0) or int(textSemestre.get()) < 1 or int(textSemestre.get()) > 10:
                    messagebox.showerror(message = "Verifique que este ingresando bien sus datos", title = "Valor Incorrecto")

                else:
                    # Enviando datos a clase Cursos
                    curso = Cursos(
                        textCodigo.get(), 
                        textNombre.get(), 
                        textPre_requisito.get(), 
                        textOpcionalidad.get(), 
                        textSemestre.get(), 
                        textCreditos.get(),
                        textEstado.get())

                    self.list_global.append(curso)

                    messagebox.showinfo(message = "Ha sido agregado con exito", title = "Curso Añadido")
                    print("Curso agregado con exito")

                    #Reseteando valores
                    textCodigo.delete(0, END)
                    textNombre.delete(0, END) 
                    textPre_requisito.delete(0, END)
                    textSemestre.delete(0, END)
                    textOpcionalidad.delete(0, END)
                    textCreditos.delete(0, END)
                    textEstado.delete(0, END)
            
        #Buttons
        botonAgregar = tk.Button(
            ventanaA, 
            text="Agregar",
            font=("Centaur", 11, "bold"),
            command = addCurso,
            width=10,
            padx=15,
            pady=5
            ).place(x=225, y=385)
        
        def regresar():
            ventanaA.withdraw()
            self.gestionarCursos()

        botonRegresar = tk.Button(
            ventanaA, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = regresar,
            width=10,
            padx=15,
            pady=5
            ).place(x=373, y=385)

    ### Funcion para editar un curso
    def editarCurso(self):

        #Configuracion ventana
        ventanaE = tk.Toplevel(self)
        ventanaE.title("Editar Curso") #Titulo de la ventana
        ventanaE.resizable(False, False) #Editable
        ventanaE.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventanaE, 550, 480)
        ventanaE.configure(
            bg="#4F4E4E", 
            width="550", 
            height="480", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )

        #Labels
        tk.Label(ventanaE, text="Codigo: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=35)
        tk.Label(ventanaE, text="Nombre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=85)
        tk.Label(ventanaE, text="Pre requisito: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=135)
        tk.Label(ventanaE, text="Semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=185)
        tk.Label(ventanaE, text="Opcionalidad: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=235)
        tk.Label(ventanaE, text="Creditos: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=285)
        tk.Label(ventanaE, text="Estado", bg="#4F4E4E", fg="White", font=("Centaur", 15, "bold")).place(x=40, y=335)

        #Cajas de texto
        edit_codigo = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_nombre = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_pre_requisito = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_semestre = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_opcionalidad = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_creditos = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        edit_estado = tk.Entry(ventanaE, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))

        #Posicion cajas de texto
        edit_codigo.place(x=180, y=35, width=320)
        edit_nombre.place(x=180, y=85, width=320)
        edit_pre_requisito.place(x=180, y=135, width=320)
        edit_semestre.place(x=180, y=185, width=320)
        edit_opcionalidad.place(x=180, y=235, width=320)
        edit_creditos.place(x=180, y=285, width=320)
        edit_estado.place(x=180, y=335, width=320)


        ##Funcion para buscar el curso
        def editCurso():

            temporal = False
            
            #Iterando en lista global
            for i in range(len(self.list_global)):

                ##Verificando que exista el codigo
                if edit_codigo.get() == self.list_global[i].getCodigo():

                    #Editando valores
                    self.list_global[i].nombre = edit_nombre.get()
                    self.list_global[i].prerequisito = edit_pre_requisito.get()

                    ##Verificando que el semestre este entre 1 y 10
                    if int(edit_semestre.get()) < 1 or int(edit_semestre.get()) > 10:
                        messagebox.showerror(message="Esta ingresando un dato incorrecto", title="Datos erroneos")
                        edit_semestre.delete(0, END)
                        temporal = True
                        break
                    else:
                        self.list_global[i].semestre = edit_semestre.get()

                    ##Verificando que los creditos sean mayor a 0
                    if int(edit_creditos.get()) < 0:
                        messagebox.showerror(message="Esta ingresando un dato incorrecto", title="Datos erroneos")
                        edit_creditos.delete(0, END)
                        temporal = True
                        break
                    else:
                        self.list_global[i].creditos = edit_creditos.get()

                    ##Verificando que la opcionalidad sea 0 o 1
                    if edit_opcionalidad.get() != "0" and edit_opcionalidad.get() != "1":
                        messagebox.showerror(message="Esta ingresando un dato incorrecto", title="Datos erroneos")
                        edit_opcionalidad.delete(0, END)
                        temporal = True
                        break
                    else:
                        self.list_global[i].obligatorio = edit_opcionalidad.get() 

                    ##Verificando que el estado sea 0, -1 o 1
                    if edit_estado.get() != "0" and edit_estado.get() != "1" and edit_estado.get() != "-1":
                        messagebox.showerror(message="Esta ingresando un dato incorrecto", title="Datos erroneos")
                        edit_estado.delete(0, END)
                        temporal = True
                        break  
                    else: 
                        self.list_global[i].estado = edit_estado.get()

                    #Reseteando valores
                    edit_codigo.delete(0, END)
                    edit_nombre.delete(0, END)
                    edit_pre_requisito.delete(0, END) 
                    edit_semestre.delete(0, END)
                    edit_opcionalidad.delete(0, END)
                    edit_creditos.delete(0, END)
                    edit_estado.delete(0, END)

                    messagebox.showinfo(message="Curso editado correctamente", title="Curso Editado")

                    temporal = True

            if temporal == False:
                messagebox.showinfo(message="El curso no existe", title="Codigo incorrecto")
        
        #Buttons
        botonEditar = tk.Button(
            ventanaE, 
            text="Editar",
            font=("Centaur", 11, "bold"),
            command = editCurso,
            width=10,
            padx=15,
            pady=5
            ).place(x=225, y=390)
        
        ##Funcion para cerrar ventana
        def regresar():
            ventanaE.withdraw()
            self.gestionarCursos()

        botonRegresar = tk.Button(
            ventanaE, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = regresar,
            width=10,
            padx=15,
            pady=5
            ).place(x=373, y=390)

    ### Funcion para eliminar curso
    def eliminarCurso(self):

        #Configuracion ventana
        ventanaEli = tk.Toplevel(self)
        ventanaEli.title("Eliminar Curso") #Titulo de la ventana
        ventanaEli.resizable(False, False) #Editable
        ventanaEli.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventanaEli, 500, 200)
        ventanaEli.configure(
            bg="#4F4E4E", 
            width="500", 
            height="200", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )

        #Label
        tk.Label(ventanaEli, text="Código de Curso: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=50, y=50)

        #Caja de texto
        text_codigo = tk.Entry(ventanaEli, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))

        #Posicion Caja de texto
        text_codigo.place(x=210, y=50, width=230)

        ## Funcion para eliminar curso
        def deleteCurso():
            temporal = False
            
            #Iterando en lista global
            for i in range(len(self.list_global)):

                ##Verificando que exista el codigo
                if text_codigo.get() == self.list_global[i].getCodigo():

                    #Eliminado elemento
                    self.list_global.pop(i)

                    #Reset caja de codigo
                    text_codigo.delete(0, END)

                    messagebox.showinfo(message="Curso eliminado correctamente", title="Elimar")
                    temporal = True
                    break

            if temporal == False:
                messagebox.showinfo(message="El curso no existe", title="Codigo incorrecto")
        
        #Buttons
        botonEliminar = tk.Button(
            ventanaEli, 
            text="Eliminar",
            command = deleteCurso,
            font=("Centaur", 11, "bold"),
            ).place(x=280, y=100)

        ## Funcion para cerrar ventana
        def regresar():
            ventanaEli.withdraw()
            self.gestionarCursos()

        botonRegresar = tk.Button(
            ventanaEli, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command=regresar
            ).place(x=370, y=100)


    #Funcion Conteo de creditos
    def conteoCreditos(self):
        
        #Configuracion ventana
        ventana = tk.Toplevel(self)
        ventana.title("Conteo de Créditos") #Titulo de la ventana
        ventana.resizable(False, False) #Editable
        ventana.iconbitmap("icono.ico") #Icono de la ventana
        self.centrar(ventana, 500, 500)
        ventana.configure(
            bg="#4F4E4E", 
            width="500", 
            height="500", 
            bd=20, 
            relief="groove", 
            cursor="spider"
        )

        #Labels
        tk.Label(ventana, text="Créditos aprobados: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=110, y=35)
        tk.Label(ventana, text="Créditos cursando: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=120, y=85)
        tk.Label(ventana, text="Créditos pendientes: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=110, y=135)
        tk.Label(ventana, text="Créditos hasta el semestre N: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=40, y=185)
        tk.Label(ventana, text="Créditos del semestre: ", fg="White", bg="#4F4E4E", font=("Centaur", 15, "bold")).place(x=90, y=275)

        labelAprobados = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelCursando = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelPendientes = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelN = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        labelSemestre = tk.Label(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))

        #Caja de texto
        semestre_N = tk.Entry(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))
        semestre = tk.Entry(ventana, fg="Black", bg="#ACACAC", font=("Centaur", 15, "bold"))

        #Posicion de widgets
        semestre_N.place(x=300, y=185, width=30)
        semestre.place(x=300, y=275, width=30)
        
        labelAprobados.place(x=375, y=35, width=50)
        labelCursando.place(x=375, y=85, width=50)
        labelPendientes.place(x=375, y=135, width=50)
        labelN.place(x=375, y=185, width=50)
        labelSemestre.place(x=375, y=275, width=50)

        ## Funcion para contar creditos hasta el semestre N
        def countN():
            
            c_obligatorio = tk.StringVar()
            _semestreN = semestre_N.get() #Obtener el texto de caja de texto
            cont_N = 0 #Sumador de creditos

            # Validar que se este ingresando un semestre valido
            if int(_semestreN) < 1 or int(_semestreN) > 10:
                messagebox.showerror(message="El numero de semestre que ingreso es incorrecto", title="Error en semestre N")

            else:
                for i in range(len(self.list_global)):

                    if int(self.list_global[i].getSemestre()) <= int(_semestreN) and self.list_global[i].getObligatorio() == "Obligatorio":

                        cont_N += int(self.list_global[i].creditos)

            c_obligatorio.set(str(cont_N))

            labelN.config(textvariable=c_obligatorio)
        
        #Buttons
        botonContarN = tk.Button(
            ventana, 
            text="Contar",
            font=("Centaur", 10, "bold"),
            command=countN,
            width=8,
            padx=8,
            pady=5
            ).place(x=195, y=228)

        ## Funcion para contar creditos de un semestre como tal
        def countS():
            
            c_creditos = tk.StringVar()
            _semestreS = semestre.get() #Obtener el texto de caja de texto
            cont_S = 0 #Sumador de creditos

            # Validar que se este ingresando un semestre valido
            if int(_semestreS) < 1 or int(_semestreS) > 10:
                messagebox.showerror(message="El numero de semestre que ingreso es incorrecto", title="Error en semestre N")

            else:
                for i in range(len(self.list_global)):

                    if int(self.list_global[i].getSemestre()) == int(_semestreS):

                        cont_S += int(self.list_global[i].creditos)

            c_creditos.set(str(cont_S))

            labelSemestre.config(textvariable=c_creditos)

        #Buttons
        botonContarS = tk.Button(
            ventana, 
            text="Contar",
            font=("Centaur", 10, "bold"),
            command=countS,
            width=8,
            padx=8,
            pady=5
            ).place(x=195, y=320)

        def cerrar():
            self.deiconify()
            ventana.destroy()

        botonRegresar = tk.Button(
            ventana, 
            text="Regresar",
            font=("Centaur", 11, "bold"),
            command = cerrar,
            width=10,
            padx=15,
            pady=5
            ).place(x=300, y=390)

        def countCreditos():

            #Contadores
            _aprobados = 0
            _cursando = 0
            _pendiente = 0
            
            #Ciclo para sumar creditos
            for i in range(len(self.list_global)):
                
                if self.list_global[i].getEstado() == "Aprobado": 
                    _aprobados += int(self.list_global[i].getCreditos())
                if self.list_global[i].getEstado() == "Cursando":
                    _cursando += int(self.list_global[i].getCreditos())
                if self.list_global[i].getEstado() == "Pendiente" and self.list_global[i].getObligatorio() == "Obligatorio":  
                    _pendiente += int(self.list_global[i].getCreditos())
            
            print(_aprobados)
            print(_cursando)
            print(_pendiente)
            
            c_aprobado = tk.StringVar()
            c_cursando = tk.StringVar()
            c_pendiente = tk.StringVar()
            
            c_aprobado.set(str(_aprobados))
            c_cursando.set(str(_cursando))
            c_pendiente.set(str(_pendiente))
            
            labelAprobados.config(textvariable=c_aprobado)
            labelCursando.config(textvariable=c_cursando)
            labelPendientes.config(textvariable=c_pendiente)

        botonContar = tk.Button(
            ventana, 
            text="Contar Creditos",
            font=("Centaur", 11, "bold"),
            command = countCreditos,
            width=10,
            padx=15,
            pady=5
            ).place(x=150, y=390)


if __name__ == "__main__":
    menuPrincipal = Menu()
    menuPrincipal.mainloop()