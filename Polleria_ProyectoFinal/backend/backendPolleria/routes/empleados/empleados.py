from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import Empleado
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appempleado = Blueprint('appempleado',__name__)

@appempleado.route('/Empleado/registro',methods = ['POST'])

def registrarEmpleado():
    responses = request.get_json()
    usuario = responses['usuario']
    response = responses['datosEmpleado']
    if(usuario['itsAdmin']):
        empleadoExist = Empleado.query.filter_by(email=response['email']).first()
        if not empleadoExist:
            empleadoR = Empleado(
                email=response['email'],
                contraseña=response['contraseña'],
                )
            empleadoR.nombre = response['nombre']
            empleadoR.puesto = response['puesto']
            empleadoR.salario = response['salario']
            empleadoR.idSucursal = response['idSucursal']
            empleadoR.admin = response['admin']
            try:
                db.session.add(empleadoR)
                db.session.commit()
                mensaje="Empleado creado"
            except exc.SQLAlchemyError as e:
                mensaje  = e
        else:
            mensaje = "Empleado existente" 
    else:
        mensaje = 'Acceso denegado' 
    return jsonify({"message":mensaje})

@appempleado.route('/Empleados/login',methods = ["POST"])
def login_post():
        response = request.get_json()
        email = response['email']
        password=response['contraseña']
        usuario = Empleado(email=email,contraseña=password)
        userFilter=Empleado.query.filter_by(email=usuario.email).first()
        if userFilter:
            validation=bcrypt.check_password_hash(userFilter.contraseña,password)
            if validation:
                auth_token = usuario.encode_auth_token(userFilter.idEmpleado)
                
                response= {
                    'status':'success',
                    'message':'Loggin exitoso',
                    'auth_token':auth_token,
                    'usuario':userFilter.nombre,
                    'itsAdmin':userFilter.admin,
                    'idEmpleado':userFilter.idEmpleado
                }
                return jsonify(response)
        return jsonify({"message":"email o contraseña inválidos"})
    

@appempleado.route('/Empleados',methods=["GET"])
@tokenCheck
def getUsers(usuario):
    if(usuario['admin']):
        response=[]
        usuarios = Empleado.query.all()
        for usuario in usuarios:
            usuarioData={
                'id':usuario.idEmpleado,
                'email':usuario.email,
                'contraseña':usuario.contraseña,
                'admin':usuario.admin,
                'nombre':usuario.nombre,
                'puesto':usuario.puesto,
                'salario':usuario.salario
            }
            response.append(usuarioData)
        return jsonify({'empleados':response})  
    else: 
        return jsonify({"message":"Acceso denegado"}) 

@appempleado.route('/Empleados/<id>', methods=["PUT"])
@tokenCheck
def Actualizar_Empleado(usuario,id):
    response = request.get_json()
    
    if(usuario['admin']):
        empleadoR = Empleado.query.get(id)
        if not empleadoR:
            return jsonify({'message': 'Empleado no encontrado'}), 404
        response = request.get_json()
        for k,v in response.items():
             setattr(empleadoR,k,v)
        try:
                db.session.commit()
                mensaje = 'Empleado actualizado con éxito'
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje})
    else: 
        return jsonify({"message":"Acceso denegado"}) 

@appempleado.route('/Empleados/<id>',methods=['DELETE'])
@tokenCheck
def Eliminar_Empleado(usuario,id):
     if(usuario['admin']):
          empleadoR = Empleado.query.get(id)
          if not empleadoR:
            return jsonify({'message': 'Empleado no encontrado'}), 404
          try:
                db.session.delete(empleadoR)
                db.session.commit()
                mensaje = 'Empleado eliminado con éxito'
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})
     else: 
        return jsonify({"message":"Acceso denegado"}) 
     
@appempleado.route('/Empleados/buscar/<nombre>',methods = ['GET'])
@tokenCheck
def BuscarEmpleado_Nombre(usuario,nombre):
     if(usuario['admin']):
          empleadoR = Empleado.query.filter_by(nombre=nombre).first()
          if not empleadoR:
            return jsonify({'message': 'Empleado no encontrado'}), 404
          try:
                response = {
                'id':empleadoR.idEmpleado,
                'email':empleadoR.email,
                'contraseña':empleadoR.contraseña,
                'admin':empleadoR.admin,
                'nombre':empleadoR.nombre,
                'puesto':empleadoR.puesto,
                'salario':empleadoR.salario
                }
                
                mensaje = [response]
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'empleados':mensaje})
     else: 
        return jsonify({"empleados":"Acceso denegado"}) 
    
@appempleado.route('/Empleados/<int:id>', methods=['GET'])
@tokenCheck
def BuscarEmpleado_Id(usuario, id):
    empleadoR = Empleado.query.get(id)
    if(usuario['admin']):
        if not empleadoR:
            return jsonify({'message': 'Empleado no encontrado'}), 404
        try:
            response = {
                'id': empleadoR.idEmpleado,
                'nombre': empleadoR.nombre,
                'email': empleadoR.email,
                'contraseña': empleadoR.contraseña,
                'puesto': empleadoR.puesto,
                'salario': empleadoR.salario,
                'admin': empleadoR.admin,
                'idSucursal': empleadoR.idSucursal
            }
            mensaje = response
        except exc.SQLAlchemyError as e:
            mensaje = str(e)
        return jsonify({'message': mensaje})
    else:
        return jsonify({"message": "Acceso denegado"})