import jwt
import datetime
from config import BasicConfig
from app import db,bcrypt


class Empleado(db.Model):
    __tablename__="Empleados"
    idEmpleado = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(255),unique=True,nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    contraseña = db.Column(db.String(255),nullable=False)
    puesto = db.Column(db.String(255),nullable=False)
    salario = db.Column(db.Float,nullable=False)
    idSucursal = db.Column(db.Integer,db.ForeignKey('Sucursales.idSucursal'))
    admin=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,email,contraseña,admin=False):
        self.email=email
        self.contraseña=bcrypt.generate_password_hash(
            contraseña,BasicConfig.BCRYPT_LOG_ROUNDS
        ).decode()
        self.admin=admin

    def encode_auth_token(self,id_Empleado):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(days=30,hours=10),
                'iat':datetime.datetime.utcnow(),
                'sub':id_Empleado
            }
            return jwt.encode(
                payload,
                BasicConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload=jwt.decode(
                auth_token,
                BasicConfig.SECRET_KEY,
                algorithms=["HS256"]
            )
            return payload['sub']
        except jwt.ExpiredSignatureError as e:
            print(e)
            return "token expirado"
        except jwt.InvalidTokenError as e:
            return "token invalido"


class Sucursal(db.Model):
    __tablename__="Sucursales"
    idSucursal = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(255),unique=True,nullable=False)
    direccion = db.Column(db.String(255),nullable=False)
    telefono = db.Column(db.String(15),nullable=False)
    correo_electronico = db.Column(db.String(60),nullable=False)



class Pedido(db.Model):
    __tablename__="Pedidos"
    idPedido = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombreCliente= db.Column(db.String(255),unique=True,nullable=False)
    direccionCliente = db.Column(db.String(255),nullable=False)
    fecha_hora = db.Column(db.DateTime,nullable=False)
    descripcion = db.Column(db.String(255),nullable=False)
    estatus = db.Column(db.String(60),nullable=False)
    total = db.Column(db.Float,nullable=False)

    
class Menu(db.Model):
    __tablename__="Menus"
    idMenu = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(255),unique=True,nullable=False)
    descripcion = db.Column(db.String(255),nullable=False)
    precio = db.Column(db.Float,nullable=False)
    imagen = db.Column(db.String(255),nullable=False)

class Comentarios_Calificaciones(db.Model):
    __tablename__ = 'Comentarios_Calificaciones'
    idComentario_Calif = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_cliente = db.Column(db.String(255),nullable=False)
    nombre_producto = db.Column(db.String(255),nullable=False)
    comentario = db.Column(db.String(255),nullable=False)
    calificacion = db.Column(db.Integer,nullable=False)
    fecha_hora = db.Column(db.DateTime,nullable=False)

class HistorialPedidos(db.Model):
    __tablename__ = 'HistorialPedidos'
    idHistorial = db.Column(db.Integer,primary_key=True,autoincrement=True)
    pedido = db.Column(db.String(255),nullable=False)
    fecha_hora = db.Column(db.DateTime,nullable=False)
    estatus = db.Column(db.String(60),nullable=False)
    comentario = db.Column(db.String(255),nullable=False)
    idEmpleado = db.Column(db.Integer,db.ForeignKey('Empleados.idEmpleado'))
    total = db.Column(db.Float,nullable=False)
