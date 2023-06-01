from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import Menu
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appmenu = Blueprint('appmenu',__name__)
@appmenu.route('/Menus/agregar',methods = ['POST'])
def agregarMenu():
        json = request.get_json()
        menuExist = Menu.query.filter_by(nombre=json['nombre']).first()
        if not menuExist:
            menu = Menu()
            menu.nombre = json['nombre']
            menu.descripcion = json['descripcion']
            menu.precio = json['precio']
            menu.imagen = json['imagen']
            try:
                db.session.add(menu)
                db.session.commit()
                mensaje = "Menu creado"
            except exc.SQLAlchemyError as ex:
                mensaje = ex
        else:
            mensaje = "Menu existente" 
        return jsonify({"message":mensaje})

@appmenu.route('/Menus',methods =["GET"])
def getMenus():
        response=[]
        menus = Menu.query.all()
        for menu in menus:
            usuarioData={
                'id':menu.idMenu,
                'nombre':menu.nombre,
                'descripcion':menu.descripcion,
                'precio':menu.precio,
                'imagen':menu.imagen,
            }
            response.append(usuarioData)
        return jsonify({'menu':response})
    
@appmenu.route('/Menus/<id>',methods =["GET"])
def getMenusId(id):
        menu = Menu.query.filter_by(idMenu=id).first()
        if not menu:
            return jsonify({'message': 'Menu no encontrado'}), 404
        try:
                response = {
                'id':menu.idMenu,
                'nombre':menu.nombre,
                'descripcion':menu.descripcion,
                'precio':menu.precio,
                'imagen':menu.imagen,
                }
                
                mensaje = response
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje})

@appmenu.route('/Menus/editar/<id>',methods=['PUT'])
def Actualizar_Menus(id):
        menu = Menu.query.get(id)
        if not menu:
            return jsonify({'message': 'Menu no encontrado'}), 404
        response = request.get_json()
        for k,v in response.items():
             setattr(menu,k,v)
        try:
                db.session.commit()
                mensaje = 'Menu actualizado con éxito'
        except exc.SQLAlchemyError as e:
                mensaje  = e

        return jsonify({'message':mensaje})

@appmenu.route('/Menus/eliminar/<id>',methods=['DELETE'])
def Eliminar_Menus(id):
          menu = Menu.query.get(id)
          if not menu:
            return jsonify({'message': 'Menu no encontrado'}), 404
          try:
                db.session.delete(menu)
                db.session.commit()
                mensaje = 'Menu eliminado con éxito'
          except exc.SQLAlchemyError as e:
                mensaje  = e

          return jsonify({'message':mensaje})

@appmenu.route('/Menus/buscar/<nombre>', methods = ['GET'])
def BuscarMenu_Nombre(nombre):
    menu = Menu.query.filter_by(nombre=nombre).first()
    if not menu:
        return jsonify({'message': 'Menu no encontrado'}), 404
    try:
        response = {
            'id': menu.idMenu,
            'nombre': menu.nombre,
            'descripcion': menu.descripcion,
            'precio': menu.precio,
            'imagen': menu.imagen,
        }
        mensaje = [response]  # Colocar el objeto de respuesta en una lista
    except exc.SQLAlchemyError as e:
        mensaje = e

    return jsonify({'menu': mensaje})