from app import db

class Psicologo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    sueldo = db.Column(db.Integer)
    
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    telefono = db.Column(db.String(250))
    edad = db.Column(db.Integer)
    monto = db.Column(db.Integer)
    
class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
    telefono = db.Column(db.Integer)
    
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    puesto = db.Column(db.String(250))
    sueldo = db.Column(db.Integer)
    correo = db.Column(db.String(250))
    departamento = db.Column(db.String(250))
    
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    
    