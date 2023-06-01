from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import Comentarios_Calificaciones
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appCC = Blueprint('appCC',__name__)

@appCC.route('/Com-Calif/agregar',methods = ['POST'])
def registrarCC():
     json = request.get_json()
     ccExist = Comentarios_Calificaciones.query.filter_by(nombre_cliente=json['nombre_cliente']).first()
     if not ccExist:
        cc = Comentarios_Calificaciones()
        cc.nombre_cliente = json['nombre_cliente']
        cc.nombre_producto = json['nombre_producto']
        cc.comentario = json['comentario']
        cc.calificacion = json['calificacion']
        cc.fecha_hora = json['fecha_hora']
        try:
            db.session.add(cc)
            db.session.commit()
            mensaje = "Cc creado"
        except exc.SQLAlchemyError as ex:
            mensaje = ex
     else:
            mensaje = "Cc existente" 
     return jsonify({"message":mensaje})


@appCC.route('/Com-Calif',methods = ['GET'])
def getCC():
        response=[]
        ccData = Comentarios_Calificaciones.query.all()
        for cc in ccData:
            usuarioData={
                'id':cc.idComentario_Calif,
                'nombre_cliente':cc.nombre_cliente,
                'nombre_producto':cc.nombre_producto,
                'comentario':cc.comentario,
                'calificacion':cc.calificacion,
                'fecha_hora':cc.fecha_hora
            }
            response.append(usuarioData)
        return jsonify({'CC':response})

@appCC.route('/Com-Calif/<id>',methods=['PUT'])
def Actualizar_CC(id):
        ccData = Comentarios_Calificaciones.query.get(id)
        if not ccData:
            return jsonify({'message': 'Comentario no encontrado'}), 404
        response = request.get_json()
        for k,v in response.items():
             setattr(ccData,k,v)
        try:
                db.session.commit()
                mensaje = 'Comentario actualizado con éxito'
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje}) 

@appCC.route('/Com-Calif/<id>',methods=['DELETE'])
@tokenCheck
def Eliminar_CC(usuario,id):
        if(usuario['admin']):
          cc = Comentarios_Calificaciones.query.get(id)
          if not cc:
            return jsonify({'message': 'Comentario no encontrado'}), 404
          try:
                db.session.delete(cc)
                db.session.commit()
                mensaje = 'Comentario eliminado con éxito'
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})
        else: 
         return jsonify({"message":"Acceso denegado"})

@appCC.route('/Com-Calif/<nombre>',methods=['GET'])
def BuscarCC_Nombre(nombre):
          cc = Comentarios_Calificaciones.query.filter_by(nombre_cliente=nombre).first()
          if not cc:
            return jsonify({'message': 'Comentario no encontrado'}), 404
          try:
                response = {
                'id':cc.idComentario_Calif,
                'nombre_cliente':cc.nombre_cliente,
                'nombre_producto':cc.nombre_producto,
                'comentario':cc.comentario,
                'calificacion':cc.calificacion,
                'fecha_hora':cc.fecha_hora
                }
                
                mensaje = response
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje}) 
