from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import HistorialPedidos
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appHistorial = Blueprint('appHistorial',__name__)

@appHistorial.route("/Historial/agregar",methods = ['POST'])
def agregarHistorial():
        json = request.get_json()
        print(json)
        historialExist = HistorialPedidos.query.filter_by(pedido=json['pedido']).first()
        if not historialExist:
            historial = HistorialPedidos()
            historial.pedido = json['pedido']
            historial.fecha_hora = json['fecha_hora']
            historial.estatus = json['estatus']
            historial.comentario = json['comentario']
            historial.idEmpleado = json['idEmpleado']
            historial.total = json['total']
            try:
                db.session.add(historial)
                db.session.commit()
                mensaje = "Historial creado"
            except exc.SQLAlchemyError as ex:
                mensaje = ex
        else:
            mensaje = "Historial existente" 
        return jsonify({"message":mensaje})
    
@appHistorial.route('/HistorialPedidos', methods=["GET"])
def getHistorialPedidos():
    response = []
    historial_pedidos = HistorialPedidos.query.all()
    for pedido in historial_pedidos:
        pedido_data = {
            'idHistorial': pedido.idHistorial,
            'pedido': pedido.pedido,
            'fecha_hora': pedido.fecha_hora,
            'estatus': pedido.estatus,
            'comentario': pedido.comentario,
            'idEmpleado': pedido.idEmpleado,
            'total': pedido.total
        }
        response.append(pedido_data)
    return jsonify({'historial_pedidos': response})

@appHistorial.route('/HistorialPedidos/<int:id>', methods=['DELETE'])
def eliminarHistorialPedido(id):
    historial_pedido = HistorialPedidos.query.get(id)
    if not historial_pedido:
        return jsonify({'message': 'Historial de pedido no encontrado'}), 404
    try:
        db.session.delete(historial_pedido)
        db.session.commit()
        mensaje = 'Historial de pedido eliminado con éxito'
    except exc.SQLAlchemyError as e:
        mensaje = str(e)
        return jsonify({'message': mensaje}), 500

    return jsonify({'message': mensaje})
from flask import jsonify

@appHistorial.route('/HistorialPedidos/buscar/<pedido>', methods=['GET'])
def buscarHistorialPedidos(pedido):
    historial_pedidos = HistorialPedidos.query.filter(HistorialPedidos.pedido.ilike(f'%{pedido}%')).all()
    if not historial_pedidos:
        return jsonify({'message': 'No se encontraron historiales de pedidos para la búsqueda especificada'}), 404

    response = []
    for historial in historial_pedidos:
        historial_data = {
            'idHistorial': historial.idHistorial,
            'pedido': historial.pedido,
            'fecha_hora': historial.fecha_hora,
            'estatus': historial.estatus,
            'comentario': historial.comentario,
            'idEmpleado': historial.idEmpleado,
            'total': historial.total
        }
        response.append(historial_data)

    return jsonify({'historial_pedidos': response})
