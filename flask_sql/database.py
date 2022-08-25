import sqlite3
from sqlite3 import Error
from tkinter import E

def sql_connection():
    try:
        con=sqlite3.connect('basedatos.db')
        return con
    except Error:
        print(Error)
def sql_insert_product(id, nombre, precio, cantidad):
    #strsql="INSERT INTO Producto(Id, Nombre, Precio, Existencia) VALUES (" + id + ",'"+nombre+"',"+ precio + ", "+ cantidad + ");"
    strsql= ('INSERT INTO producto (id, nombre, precio, existencia) VALUES (?,?,?,?)',(id,nombre, precio, cantidad))
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
    
def sql_select_products():
    strsql = "SELECT * FROM Producto;"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    productos=cursor_Obj.fetchall()
    con.close()
    return productos

def sql_edit_product(id, cantidad):
    strsql = "UPDATE Producto SET Existencia = "+cantidad+" WHERE Id= "+id+";"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_producto(id):
    strsql = "DELETE FROM Producto WHERE Id= "+id+";"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()