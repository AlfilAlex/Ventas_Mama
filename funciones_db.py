import sqlite3

def cursor():
    """Devuelve un cursor conectado a productos.db para realizar las operacion"""
    db_Con = sqlite3.connect('productos.db')
    return db_Con.cursor(), db_Con

def prod_Select():
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")
    cursor_Insert.execute("SELECT * FROM productos")
    tabla = cursor_Insert.fetchall()
    return tabla

def add_Prod(name, price):
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INT PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")
    cursor_Insert.execute("INSERT INTO productos VALUES (?, ?)", (name, price))
    print('Se agrego el producto %s con precio %s'%(name, price))

def ventas(prod_id, sell_Num):
    """Esta función debe agregar la venta a la base de datos en la tabla ventas"""
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS ventas (dia VARCHAR(30), hora VARCHAR(30), prod_id INT, sell_Num INT)")
    table_Insert((prod_id, sell_Num), funcion = 'ventas')
    print('Se agregó la venta de %s de %s ´s '%(sell_Num, prod_id))

def prod_Resum():
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")
    cursor_Insert.execute("SELECT * FROM ventas where dia = DATE()")
    tabla = cursor_Insert.fetchall()
    return tabla

def inicio():
    """Esta funcion crea la base de datos de 'productos' """
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INT PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")


def table_Insert(lista, funcion = 'ventas'):
    """Agrega a una tabla 'funcion' la lista de valores 'lista'"""
    cursor_Insert, coneccion_Insert = cursor()
    if funcion == 'ventas':
        cursor_Insert.execute('INSERT INTO ventas VALUES (DATE(), TIME(), ?, ?)', lista)
    elif funcion == 'productos':
        cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos_t (prod_ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20) UNIQUE, precio INT)")
        cursor_Insert.execute("INSERT INTO productos(nombre, precio) VALUES (?, ?)", lista)
        print('Se agrego el producto %s con precio %s'%lista)
    #Otros elif

    coneccion_Insert.commit()

def del_Product(prod_Name):
    """Permite borrar productos de la BD en la tabla productos"""
    cursor_Insert, coneccion_Insert = cursor()
    product = [prod_Name]
    cursor_Insert.execute('DELETE FROM productos WHERE nombre = ?', product)
    coneccion_Insert.commit()
    print('Se ha borrado el producto %s'%prod_Name)
    pass
        




























