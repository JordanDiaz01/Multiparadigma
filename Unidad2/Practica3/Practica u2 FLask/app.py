from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_migrate import Migrate
from database import db
from forms import menuForm, empleadosForm, pedidoForm
from models import Empleado, Menu, Pedido
import logging

app = Flask(__name__)

# Configuración de la base de datos
USER_DB = 'postgres'  # Nombre de usuario de la base de datos
PASS_DB = 'Sobrecarga2*'  # Contraseña de la base de datos
URL_DB = 'localhost'  # Dirección de la base de datos
NAME_DB = 'pollosAsados'  # Nombre de la base de datos
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'  # URL completa de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB  # Configuración de la URI de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva el seguimiento de las modificaciones a la base de datos

# Inicialización de la base de datos y migración
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

# Configuración del registro de errores
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Configuración de la llave secreta para proteger la aplicación de ataques CSRF
app.config["SECRET_KEY"] = "llave secreta"
@app.route('/')
@app.route('/index')
def inicio():
    """
    Función que maneja la ruta de la página principal. 
    Obtiene todos los elementos de la tabla Menu y el número total de menús y los pasa a la plantilla 'index.html' 
    """
    menu = Menu.query.all()  # Obtiene todos los elementos de la tabla Menu
    totalMenu = Menu.query.count()  # Obtiene el número total de menús
    app.logger.debug(f'Menu: {menu}')  # Registro de depuración
    return render_template('index.html',menu=menu,totalMenu=totalMenu)


@app.route('/agregarMenu',methods = ["GET","POST"])
def agregarMenu():
    """
    Función que maneja la ruta para agregar un nuevo menú. 
    Crea una nueva instancia del modelo de menú, instancia un formulario y valida el formulario. 
    Si el formulario es válido, se agrega el menú a la base de datos y se redirige al usuario a la página principal. 
    """
    menu = Menu()  # Crea una nueva instancia del modelo de menú
    menuform = menuForm(obj=menu)  # Instancia un formulario y lo rellena con los datos del menú
    if request.method== "POST":
        if menuform.validate_on_submit():  # Valida el formulario
            menuform.populate_obj(menu)  # Rellena el objeto de menú con los datos del formulario
            db.session.add(menu)  # Agrega el objeto de menú a la sesión de la base de datos
            db.session.commit()  # Guarda los cambios en la base de datos
            app.logger.debug(f'dato agregado: {menu}')  # Registro de depuración
            return redirect(url_for('inicio'))  # Redirige al usuario a la página principal
    return render_template('./Menu/agregarMenu.html',forma=menuform)


@app.route('/editarMenu/<int:id>',methods = ["GET","POST"])
def editarMenu(id):
    """
    Función que maneja la ruta para editar un menú existente. 
    Obtiene el menú correspondiente al ID proporcionado, instancia un formulario y valida el formulario. 
    Si el formulario es válido, se actualiza el menú en la base de datos y se redirige al usuario a la página principal. 
    """
    menu = Menu.query.get_or_404(id)  # Obtiene el menú correspondiente al ID proporcionado o devuelve un error 404 si no existe
    menuform = menuForm(obj=menu)  # Instancia un formulario y lo rellena con los datos del menú
    if request.method== "POST":
        if menuform.validate_on_submit():  # Valida el formulario
            menuform.populate_obj(menu)  # Rellena el objeto de menú con los datos del formulario
            db.session.commit()  # Guarda los cambios en la base de datos
            app.logger.debug(f'Actualizado: {menu}')  # Registro de depuración
        return redirect(url_for('inicio'))  # Redirige al usuario a la página principal
    return render_template('./Menu/editarMenu.html',forma=menuform)


@app.route('/eliminarMenu/<int:id>')
def eliminarMenu(id):
    """ 
    Función que maneja la ruta para eliminar un menú existente. 
    Obtiene el menú correspondiente al ID proporcionado, lo elimina de la base de datos
    """
    menu = Menu.query.get_or_404(id)
    db.session.delete(menu)
    db.session.commit()
    app.logger.debug(f'dato eliminado: {menu}')
    return redirect(url_for('inicio'))

@app.route('/empleados')
def inicioE():
    """
    La función 'inicioE' maneja la ruta '/empleados' y muestra una lista de todos los empleados en la base de datos.
    Retorna una plantilla HTML renderizada que muestra una tabla con los datos de todos los empleados y el número total de empleados.

    Returns:
    - render_template: función que renderiza una plantilla HTML que muestra la lista de empleados y el número total de empleados.
    """
    empleado = Empleado.query.all() # Obtiene todos los empleados de la base de datos
    totalEmpleados = Empleado.query.count() # Obtiene el número total de empleados en la base de datos
    app.logger.debug(f'listado de empleados: {empleado}') # Imprime en la consola el listado de empleados obtenidos
    return render_template('./Empleado/index.html',empleado=empleado,totalEmpleados=totalEmpleados)


@app.route('/empleados/agregarEmpleado',methods = ["GET","POST"])
def agregarEmpleado():
    """
    La función 'agregarEmpleado' maneja la ruta '/empleados/agregarEmpleado' y permite agregar un nuevo empleado a la base de datos.
    Si se realiza una solicitud 'POST', se valida y se agrega el nuevo empleado a la base de datos. Si la validación falla, se muestra un mensaje de error.
    Si se realiza una solicitud 'GET', se muestra el formulario para agregar un nuevo empleado.

    Returns:
    - render_template: función que renderiza una plantilla HTML que muestra el formulario para agregar un nuevo empleado.
    - redirect: función que redirige a la ruta '/empleados' una vez que se ha agregado un nuevo empleado a la base de datos.
    """
    empleado = Empleado() # Crea un nuevo objeto Empleado vacío
    empleadoForm = empleadosForm(obj=empleado) # Crea un formulario utilizando el objeto Empleado vacío
    if request.method == "POST": # Si se realizó una solicitud 'POST'
        if empleadoForm.validate_on_submit(): # Si el formulario fue validado con éxito
            empleadoForm.populate_obj(empleado) # Rellena el objeto Empleado con los datos del formulario
            db.session.add(empleado) # Agrega el objeto Empleado a la sesión de la base de datos
            db.session.commit() # Guarda los cambios en la base de datos
            app.logger.debug(f'dato agregado: {empleado}') # Imprime en la consola el nuevo objeto Empleado agregado
            return redirect(url_for('inicioE')) # Redirige a la ruta '/empleados'
    return render_template('./Empleado/agregar.html',forma=empleadoForm) # Renderiza una plantilla HTML que muestra el formulario para agregar un nuevo empleado.


@app.route('/empleados/editarEmpleado/<int:id>', methods=["GET", "POST"])
def editarEmpleado(id):
    # Recuperar el objeto Empleado con el ID proporcionado o devolver un error 404
    empleado = Empleado.query.get_or_404(id)

    # Crear un formulario de edición de Empleado, inicializado con los detalles del objeto Empleado recuperado
    empleadoForm = empleadosForm(obj=empleado)

    # Si la solicitud HTTP es un POST (es decir, si se ha enviado un formulario)
    if request.method == "POST":

        # Validar el formulario de edición del empleado
        if empleadoForm.validate_on_submit():

            # Actualizar los valores del objeto Empleado con los valores enviados en el formulario
            empleadoForm.populate_obj(empleado)

            # Guardar los cambios en la base de datos
            db.session.commit()

            # Registrar el cambio realizado en la aplicación
            app.logger.debug(f'dato editado: {empleado}')

            # Redireccionar al usuario a la página de inicio de empleados
            return redirect(url_for('inicioE'))

    # Si la solicitud HTTP es un GET, renderizar la plantilla para el formulario de edición del empleado
    # con el formulario de Empleado ya creado e inicializado
    return render_template('./Empleado/editarEmpleado.html', forma=empleadoForm)


@app.route('/empleados/eliminarEmpleado/<int:id>')
def eliminarEmpleado(id):
    # Recuperar el objeto Empleado con el ID proporcionado o devolver un error 404
    empleado = Empleado.query.get_or_404(id)

    # Eliminar el objeto Empleado de la base de datos
    db.session.delete(empleado)
    db.session.commit()

    # Registrar la eliminación realizada en la aplicación
    app.logger.debug(f'dato eliminado: {empleado}')

    # Redireccionar al usuario a la página de inicio de empleados
    return redirect(url_for('inicioE'))


@app.route('/pedidos')
def inicioP():
    # Recuperar todos los objetos Pedido de la base de datos
    pedido = Pedido.query.all()

    # Contar el número total de objetos Pedido en la base de datos
    totalPedido = Pedido.query.count()

    # Registrar la lista de pedidos recuperada en la aplicación
    app.logger.debug(f'listado de pedidos: {pedido}')

    # Renderizar la plantilla para la página de inicio de pedidos con la lista de pedidos y el número total de pedidos
    return render_template('./Pedidos/index.html', pedido=pedido, totalPedido=totalPedido)


@app.route('/pedidos/agregarPedidos',methods = ["GET","POST"])
def agregarPedidos():
    # Crear una instancia vacía del objeto Pedido
    pedido = Pedido()

    # Crear un objeto pedidoForm a partir de la instancia del objeto Pedido
    pedidoform = pedidoForm(obj=pedido)

    # Si se envió una solicitud POST al servidor
    if request.method == "POST":
        # Si el formulario fue validado con éxito
        if pedidoform.validate_on_submit():
            # Rellenar la instancia del objeto Pedido con los datos del formulario
            pedidoform.populate_obj(pedido)

            # Agregar la instancia del objeto Pedido a la base de datos
            db.session.add(pedido)
            db.session.commit()

            # Registrar la adición realizada en la aplicación
            app.logger.debug(f'dato agregado: {pedido}')

            # Redireccionar al usuario a la página de inicio de pedidos
            return redirect(url_for('inicioP'))

    # Renderizar la plantilla para la página de agregar pedidos con el formulario para crear nuevos objetos Pedido
    return render_template('./Pedidos/agregarPedidos.html',forma=pedidoform)

@app.route('/pedidos/editarPedidos/<int:id>', methods=["GET", "POST"])
def editarPedidos(id):
    # Se busca el pedido por su ID. Si no existe, devuelve error 404.
    pedido = Pedido.query.get_or_404(id)
    # Se crea un formulario para editar el pedido, inicializado con los datos del pedido existente.
    pedidoform = pedidoForm(obj=pedido)
    # Si el formulario ha sido enviado:
    if request.method == "POST":
        # Se valida el formulario.
        if pedidoform.validate_on_submit():
            # Se actualizan los datos del pedido con los datos del formulario.
            pedidoform.populate_obj(pedido)
            # Se guarda el pedido actualizado en la base de datos.
            db.session.commit()
            # Se escribe un mensaje de depuración en el registro de la aplicación.
            app.logger.debug(f'dato editado: {pedido}')
            # Se redirige al usuario a la página de inicio de pedidos.
            return redirect(url_for('inicioP'))
    # Si el formulario no ha sido enviado, se muestra la plantilla para editar pedidos con el formulario creado.
    return render_template('./Pedidos/editarPedidos.html', forma=pedidoform)


@app.route('/pedidos/eliminarPedidos/<int:id>')
def eliminarPedidos(id):
    # Se busca el pedido por su ID. Si no existe, devuelve error 404.
    pedido = Pedido.query.get_or_404(id)
    # Se elimina el pedido de la base de datos.
    db.session.delete(pedido)
    db.session.commit()
    # Se escribe un mensaje de depuración en el registro de la aplicación.
    app.logger.debug(f'dato eliminado: {pedido}')
    # Se redirige al usuario a la página de inicio de pedidos.
    return redirect(url_for('inicioP'))


#http menu:

@app.route('/menuhttp/agregar', methods=["POST"])
def agregarMenuHttp():
    try:
        # Se recibe el JSON enviado por la petición POST.
        json = request.get_json()
        # Se crea un objeto Menu con los datos del JSON.
        menu = Menu()
        menu.nombreProducto = json['nombreProducto']
        menu.Descripcion = json['Descripcion']
        menu.Costo = json['Costo']
        # Se agrega el objeto Menu a la sesión de la base de datos y se guarda.
        db.session.add(menu)
        db.session.commit()
        # Se escribe un mensaje de depuración en el registro de la aplicación.
        app.logger.debug(f'Menu agregado: {menu}')
        # Se devuelve una respuesta JSON indicando el éxito de la operación.
        return jsonify({"status": 200, "mensaje": "menu actualizado"})
    except Exception as ex:
        # En caso de que ocurra una excepción, se escribe un mensaje de error en el registro de la aplicación.
        app.logger.error(f'error al agregar: {menu}')
        # Se devuelve una respuesta JSON con un código de error y el mensaje de la excepción.
        return jsonify({"status": 400, "mensaje": ex})


@app.route('/menuhttp/editar', methods=["POST"])
def editarMenuHttp():
    try:
        # Se recibe el JSON enviado por la petición POST.
        json = request.get_json()
        # Se busca el objeto Menu por su ID en la base de datos.
        menu = Menu.query.get_or_404(json["id"])
        # Se actualizan los datos del objeto Menu con los datos del JSON.
        menu.nombreProducto = json['nombreProducto']
        menu.Descripcion = json['Descripcion']
        menu.Costo = json['Costo']
        # Se guarda el objeto Menu en la base de datos.
        db.session.commit()
        # Se escribe un mensaje de depuración en el registro de la aplicación.
        app.logger.debug(f'Menu editado: {menu}')
        # Se devuelve una respuesta JSON indicando el éxito de la operación.
        return jsonify({"status": "OK", "mensaje": "menu modificado"})
    except Exception as ex:
        # En caso de que ocurra una excepción, se escribe un mensaje de error en el registro de la aplicación.
        app.logger.error(f'error al actualizar: {menu}')
        # Se devuelve una respuesta JSON con un código de error y el mensaje de la excepción.
        return jsonify({"status": 400, "mensaje": ex})



# Ruta para eliminar un menú HTTP
@app.route('/menuhttp/eliminar', methods=["POST"])
def elimnarMenuHttp():
    try:
        # Obtiene el objeto JSON de la solicitud
        json = request.get_json()
        
        # Busca el menú en la base de datos por su ID
        menu = Menu.query.get_or_404(json["id"])
        
        # Registra en el archivo de registro que el menú fue eliminado
        app.logger.debug(f'Menu eliminado: {menu}')
        
        # Elimina el menú de la base de datos
        db.session.delete(menu)
        db.session.commit()
        
        # Retorna una respuesta JSON indicando que el menú fue eliminado exitosamente
        return jsonify({"status":"OK","mensaje":"Menu eliminado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al eliminar: {menu}')
        return jsonify({"status":400,"mensaje":ex})


# Ruta para obtener todos los menús HTTP
@app.route('/menuhttp/obtener',methods = ["GET"])
def obtenerMenuHttp():
    # Obtiene todos los menús de la base de datos
    menu = Menu.query.all()
    
    # Crea una lista vacía para almacenar los menús
    listaMenu = []
    
    # Recorre todos los menús obtenidos de la base de datos y crea un diccionario con sus atributos
    for p in menu:
        productoMenu = {}
        productoMenu["nombreProducto"] = p.nombreProducto
        productoMenu["Costo"] = p.Costo
        productoMenu["Descripcion"] = p.Descripcion
        
        # Registra en el archivo de registro el listado de menús
        app.logger.debug(f'listado Menu: {menu}')
        
        # Agrega el diccionario a la lista de menús
        listaMenu.append(productoMenu)
    
    # Retorna una respuesta JSON con la lista de menús
    return jsonify({"status":"OK","mensaje":listaMenu})
 
 #http empleado
 
# Importa los módulos necesarios de Flask y SQLAlchemy
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Crea una instancia de la aplicación

# Ruta para agregar un empleado a la base de datos
@app.route('/empleadohttp/agregar', methods=["POST"])
def agregarEmpleadoHttp():
    try:
        # Obtiene el objeto JSON de la solicitud y crea un objeto Empleado con los datos proporcionados
        json = request.get_json()
        empleado = Empleado()
        empleado.nombre = json['nombre']
        empleado.Puesto = json['Puesto']
        empleado.Sueldo = json['Sueldo']
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(empleado)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue agregado a la base de datos
        app.logger.debug(f'empleado agregado: {empleado}')
        
        # Retorna una respuesta JSON indicando que el empleado fue agregado exitosamente
        return jsonify({"status":200,"mensaje":"empleado actualizado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al agregar: {empleado}')
        return jsonify({"status":400,"mensaje":ex})

# Ruta para editar un empleado en la base de datos
@app.route('/empleadohttp/editar', methods=["POST"])
def editarEmpleadoHttp():
    try:
        # Obtiene el objeto JSON de la solicitud y busca el empleado correspondiente en la base de datos por su ID
        json = request.get_json()
        empleado = Empleado.query.get_or_404(json["id"])
        
        # Actualiza los atributos del objeto Empleado con los datos proporcionados en el objeto JSON
        empleado.nombre = json['nombre']
        empleado.Puesto = json['Puesto']
        empleado.Sueldo = json['Sueldo']
        
        # Guarda los cambios en la base de datos
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue actualizado en la base de datos
        app.logger.debug(f'empleado actualizado: {empleado}')
        
        # Retorna una respuesta JSON indicando que el empleado fue actualizado exitosamente
        return jsonify({"status":"OK","mensaje":"empleado modificado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al editar: {empleado}')
        return jsonify({"status":400,"mensaje":ex})

@app.route('/empleadohttp/eliminar',methods = ["POST"])
def elimnarEmpleadoHttp():
     try:
          # Se obtiene el objeto JSON que se envió con la petición
          json = request.get_json()
          # Se busca el empleado correspondiente en la base de datos, a partir de su ID
          empleado = Empleado.query.get_or_404(json["id"])
          # Se registra en el registro de la aplicación el empleado que se está eliminando
          app.logger.debug(f'empleado eliminado: {empleado}')
          # Se elimina el empleado de la base de datos
          db.session.delete(empleado)
          # Se confirma la eliminación en la base de datos
          db.session.commit()
          # Se devuelve una respuesta en formato JSON indicando que el empleado ha sido eliminado
          return jsonify({"status":"OK","mensaje":"empleado eliminado"})
     except Exception as ex:
            # En caso de producirse algún error, se registra en el registro de la aplicación
            app.logger.error(f'error al eliminar: {empleado}')
            # Se devuelve una respuesta en formato JSON con información sobre el error
            return jsonify({"status":400,"mensaje":ex})
     

@app.route('/empleadohttp/obtener',methods = ["GET"])
def obtenerEmpleadoHttp():
     # Se obtienen todos los empleados de la base de datos
     empleado = Empleado.query.all()
     listaEmpleados = []
     # Se recorre la lista de empleados y se crea un diccionario para cada uno, que incluye su nombre, sueldo y puesto
     for p in empleado:
          empleados = {}
          empleados["nombre"] = p.nombre
          empleados["Sueldo"] = p.Sueldo
          empleados["Puesto"] = p.Puesto
          listaEmpleados.append(empleados)
          # Se registra en el registro de la aplicación la lista de empleados que se está devolviendo
          app.logger.debug(f'listado empleados: {empleado}')
     # Se devuelve una respuesta en formato JSON con la lista de empleados
     return jsonify({"status":"OK","mensaje":listaEmpleados})
