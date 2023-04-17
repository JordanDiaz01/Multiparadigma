# Importamos la base de datos que vamos a usar (db) desde el archivo app.py
from app import db

# Creamos la clase Empleado, que hereda de db.Model (la clase base de SQLAlchemy para modelos de bases de datos)
class Empleado(db.Model):
    # Definimos las columnas que va a tener la tabla Empleado en nuestra base de datos
    # El id será un entero y será la llave primaria de la tabla
    id = db.Column(db.Integer, primary_key=True)
    # El nombre será una cadena de caracteres con longitud máxima de 250 caracteres
    nombre = db.Column(db.String(250))
    # El Puesto será una cadena de caracteres con longitud máxima de 250 caracteres
    Puesto = db.Column(db.String(250))
    # El Sueldo será un entero
    Sueldo = db.Column(db.Integer)

# Creamos la clase Menu, que también hereda de db.Model
class Menu(db.Model):
    # Definimos las columnas que va a tener la tabla Menu en nuestra base de datos
    # El id será un entero y será la llave primaria de la tabla
    id = db.Column(db.Integer, primary_key=True)
    # El nombreProducto será una cadena de caracteres con longitud máxima de 250 caracteres
    nombreProducto = db.Column(db.String(250))
    # El Costo será un entero
    Costo = db.Column(db.Integer)
    # La Descripcion será una cadena de caracteres con longitud máxima de 250 caracteres
    Descripcion = db.Column(db.String(250))

# Creamos la clase Pedido, que también hereda de db.Model
class Pedido(db.Model):
    # Definimos las columnas que va a tener la tabla Pedido en nuestra base de datos
    # El id será un entero y será la llave primaria de la tabla
    id = db.Column(db.Integer, primary_key=True)
    # El Producto será una cadena de caracteres con longitud máxima de 250 caracteres
    Producto = db.Column(db.String(250))
    # El Costo será un entero
    Costo = db.Column(db.Integer)
    # La Direccion será una cadena de caracteres con longitud máxima de 250 caracteres
    Direccion = db.Column(db.String(250))