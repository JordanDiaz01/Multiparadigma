from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import Sucursal
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appsucursal = Blueprint('appsucursal',__name__)

@appsucursal.route('/Sucursales/agregar',methods =["POST"])
@tokenCheck
def agregarSucursal(usuario):
    if(usuario['admin']):
        json = request.get_json()
        sucursalExist = Sucursal.query.filter_by(nombre=json['nombre']).first()
        if not sucursalExist:
            sucursal = Sucursal()
            sucursal.nombre = json['nombre']
            sucursal.direccion = json['direccion']
            sucursal.telefono = json['telefono']
            sucursal.correo_electronico = json['correo_electronico']
            try:
                db.session.add(sucursal)
                db.session.commit()
                mensaje = "Sucursal creada"
            except exc.SQLAlchemyError as ex:
                mensaje = ex
        else:
            mensaje = "Sucursal existente" 
        return jsonify({"message":mensaje})         
    else: 
        return jsonify({"message":"Acceso denegado"})

@appsucursal.route('/Sucursales',methods=["GET"])   
def getSucursales():
    
        response=[]
        sucursales = Sucursal.query.all()
        for sucursal in sucursales:
            usuarioData={
                'IdSucursal':sucursal.idSucursal,
                'nombre':sucursal.nombre,
                'direccion':sucursal.direccion,
                'telefono':sucursal.telefono,
                'correo_electronico':sucursal.correo_electronico
            }
            response.append(usuarioData)
        return jsonify({'sucursal':response})  
    

@appsucursal.route('/Sucursales/<id>',methods=['PUT'])
@tokenCheck
def Actualizar_Sucursal(usuario,id):
    if(usuario['admin']):
        sucursal = Sucursal.query.get(id)
        if not sucursal:
            return jsonify({'message': 'Sucursal no encontrada'}), 404
        response = request.get_json()
        for k,v in response.items():
             setattr(sucursal,k,v)
        try:
                db.session.commit()
                mensaje = 'Sucursal actualizada con éxito'
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje})
    else: 
        return jsonify({"message":"Acceso denegado"}) 

@appsucursal.route('/Sucursales/<id>',methods=['DELETE'])
@tokenCheck
def Eliminar_Sucursal(usuario,id):
     if(usuario['admin']):
          sucursal = Sucursal.query.get(id)
          if not sucursal:
            return jsonify({'message': 'Sucursal no encontrada'}), 404
          try:
                db.session.delete(sucursal)
                db.session.commit()
                mensaje = 'Sucursal eliminada con éxito'
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})
     else: 
        return jsonify({"message":"Acceso denegado"}) 


@appsucursal.route('/Sucursales/<nombre>',methods = ['GET'])
@tokenCheck
def BuscarSucursal_Nombre(usuario,nombre):
     if(usuario['admin']):
          sucursal = Sucursal.query.filter_by(nombre=nombre).first()
          if not sucursal:
            return jsonify({'sucursal': 'Sucursal no encontrada'}), 404
          try:
                response = {
                     'IdSucursal':sucursal.idSucursal,
                    'nombre':sucursal.nombre,
                    'direccion':sucursal.direccion,
                    'telefono':sucursal.telefono,
                    'correo_electronico':sucursal.correo_electronico
                }
                
                mensaje = [response]
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'sucursal':mensaje})
     else: 
        return jsonify({"sucursal":"Acceso denegado"}) 
    
@appsucursal.route('/Sucursales/buscarId/<id>',methods = ['GET'])
@tokenCheck
def BuscarSucursal_Id(usuario,id):
     if(usuario['admin']):
          sucursal = Sucursal.query.filter_by(idSucursal=id).first()
          print(sucursal)
          if not sucursal:
            return jsonify({'message': 'Sucursal no encontrada'}), 404
          try:
                response = {
                    'IdSucursal':sucursal.idSucursal,
                    'nombre':sucursal.nombre,
                    'direccion':sucursal.direccion,
                    'telefono':sucursal.telefono,
                    'correo_electronico':sucursal.correo_electronico
                }
                
                mensaje = response
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})
     else: 
        return jsonify({"message":"Acceso denegado"}) 