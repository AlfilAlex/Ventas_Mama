import tkinter as tk
import sqlite3

class mainthing(tk.Frame):
   def __init__(self,parent):
      tk.Frame.__init__(self, parent)
      self.parent = parent
      self.initialize()

   def initialize(self):

      self.parent.title("Venta_de_hoy")
      self.parent.geometry('500x400')       
      self.parent.grid_rowconfigure(0,weight=1)
      self.parent.grid_columnconfigure(0,weight=1)
      self.parent.config(background="black") 

      #self.frame = tk.Frame(self.parent, width=400, height=250)  
      self.pack(expand=1, fill=tk.BOTH)

      self.topEntry = tk.Entry(self, bg = "#006600", fg = "#00ff00")
      self.topEntry.grid(column=1, row=5, sticky="ew")


      yesBut = tk.Button(self, text="Yes")
      yesBut.grid(column=0, row=5)

      label = tk.Label(self, text="Productos_de_hoy")
      label.grid(row=0, column=0)

      #Botones -----------    -----------------   -------------
      boton_archivo = tk.Button(self, text='Agregar_productos')#, command=self.lista_de_productos)
      boton_archivo.grid(row=1, column=0, padx=20, pady=30)

      boton_agregar = tk.Button(self, text='Nuevo producto')#, command=self.agregar_producto)
      boton_agregar.grid(row=2, column=0, padx=20, pady=30)

      #Cuadros de texto ----------    -----------------   -----
      self.outputtxt = tk.Text(self, height = 10, width = 25, bg = "light yellow")
      self.outputtxt.grid(row=1, column=1, padx=20, pady=30)

      self.inputtxt = tk.Text(self, height = 10, width = 25, bg = "light yellow")
      self.inputtxt.grid(row=2, column=1, padx=20, pady=30)      
      
      self.conexion = None
      #self.list_Producto = []
      #query = tk.Label(self.frame, fg="#00ff00", bg="#001a00", anchor="w")
      #query.grid(column=1, row=0, columnspan=2, sticky="ew")

   # def lista_de_productos(self):    
   #    cursor = self.conecta_base()
   #    cursor.execute("""SELECT PRODUCTOS FROM productos""")
   #    self.list_Producto = cursor.fetchall()   
   

   # def agregar_producto(self):
   #    inputtxt = self.inputtxt.get("1.0", "end-1c")
   #    producto_to_dab = inputtxt.split(',')
   #    #Trabajo con la db
   #    cursor = self.conecta_base()
   #    cursor.execute("INSERT INTO productos (PRODUCTOS, PRECIO) VALUES (?, ?)", producto_to_dab)
   #    self.conexion.commit()
   #    cursor.execute("""SELECT PRODUCTOS FROM productos""")
   #    self.list_Producto = cursor.fetchall()

   #    self.outputtxt.delete('1.0', tk.END)
   #    for producto in self.list_Producto:
   #       self.outputtxt.insert(tk.END, producto[0] + '\n')
   #    self.inputtxt.delete('1.0', tk.END)

   
   # #Coneccion con la base
   # def conecta_base(self):
   #    self.conexion = sqlite3.connect('productos.db')
   #    cursor = self.conexion.cursor()
   #    cursor.execute("""CREATE TABLE IF NOT EXISTS productos  
   #                   (ID_PROD INTEGER PRIMARY KEY  AUTOINCREMENT, 
   #                   PRODUCTOS VARCHAR(15),
   #                   PRECIO INT)""")
   #    return cursor

   # def desconectar_base(self):
   #    self.conexion.close()


   # def venta_dia(self):
   #    self.conexion = sqlite3.connect('productos.db')
   #    cursor = self.conexion.cursor()
   #    cursor.execute("""CREATE TABLE IF NOT EXISTS venta_dia  
   #                   (ID_PROD INTEGER PRIMARY KEY  AUTOINCREMENT, 
   #                   DIA DATE,
   #                   VENTA INT)""")
                     
   #    numero_total = cursor.execute("""SELECT PRODUCTOS FROM productos""")
   #    venta_hoy = []
   #    cursor.execute("INSERT INTO productos (DIA, VENTA) VALUES (?, ?)", venta_hoy)


if __name__ == "__main__": 
   root = tk.Tk()
   app = mainthing(root)   
   root.mainloop()