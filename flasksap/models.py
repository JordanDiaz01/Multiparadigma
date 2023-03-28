from app import db

class Persona(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

class Producto(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    precio = db.Column(db.String(250))