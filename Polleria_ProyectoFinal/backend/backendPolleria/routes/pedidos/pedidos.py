from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import Pedido,HistorialPedidos
from app import db,bcrypt
from auth import tokenCheck,verificarToken

apppedido = Blueprint('apppedido',__name__)

@apppedido.route('/Pedidos/agregar',methods =["POST"])
def agregarPedido():
        json = request.get_json()
        pedidoExist = Pedido.query.filter_by(nombreCliente=json['nombreCliente']).first()
        if not pedidoExist:
            pedido = Pedido()
            pedido.nombreCliente = json['nombreCliente']
            pedido.direccionCliente = json['direccionCliente']
            pedido.fecha_hora = json['fecha_hora']
            pedido.descripcion = json['descripcion']
            pedido.estatus = json['estatus']
            pedido.total = json['total']
            try:
                db.session.add(pedido)
                db.session.commit()
                mensaje = "Pedido creado"
            except exc.SQLAlchemyError as ex:
                mensaje = ex
        else:
            mensaje = "Pedido existente" 
        return jsonify({"message":mensaje})
      
@apppedido.route('/Pedidos',methods =["GET"])
def getPedidos():
        response=[]
        pedidos = Pedido.query.all()
        for pedido in pedidos:
            usuarioData={
                'id':pedido.idPedido,
                'nombreCliente':pedido.nombreCliente,
                'direccionCliente':pedido.direccionCliente,
                'fecha_hora':pedido.fecha_hora,
                'descripcion':pedido.descripcion,
                'estatus':pedido.estatus,
                'total':pedido.total
            }
            response.append(usuarioData)
        return jsonify({'pedido':response})

@apppedido.route('/Pedidos/<id>',methods=['PUT'])
def Actualizar_Pedido(id):
        pedido = Pedido.query.get(id)
        if not pedido:
            return jsonify({'message': 'Pedido no encontrado'}), 404
        response = request.get_json()
        for k,v in response.items():
             setattr(pedido,k,v)
        try:
                db.session.commit()
                mensaje = 'Pedido actualizado con éxito'
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje})

@apppedido.route('/Pedidos/<id>',methods=['DELETE'])
def Eliminar_Pedido(id):
          pedido = Pedido.query.get(id)
          if not pedido:
            return jsonify({'message': 'Pedido no encontrado'}), 404
          try:
                db.session.delete(pedido)
                db.session.commit()
                mensaje = 'Pedido eliminado con éxito'
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})

@apppedido.route('/Pedidos/buscarNombre/<nombre>',methods = ['GET'])
def BuscarPedido_Nombre(nombre):
          print(nombre)
          pedido = Pedido.query.filter_by(nombreCliente=nombre).first()
          if not pedido:
            return jsonify({'message': 'Pedido no encontrado'}), 404
          try:
                response = {
                    'id':pedido.idPedido,
                    'nombreCliente':pedido.nombreCliente,
                    'direccionCliente':pedido.direccionCliente,
                    'fecha_hora':pedido.fecha_hora,
                    'descripcion':pedido.descripcion,
                    'estatus':pedido.estatus,
                    'total':pedido.total
                }
                
                mensaje = [response]
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'pedido':mensaje})