from flask import Flask, render_template, url_for, redirect, request, jsonify, session, abort
from flask_migrate import Migrate
from database import db
from forms import psicologoForm
from models import Psicologo, Paciente, Sucursal, Empleado, Equipo
from config import basicConfigs
import logging


app = Flask(__name__)
app.config.from_object(basicConfigs)

# Inicialización de la base de datos y migración
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

# Configuración del registro de errores
logging.basicConfig(filename='app.log', level=logging.DEBUG)

def require_login():
    allowed_routes = ['login', 'signup'] # rutas permitidas sin usuario en sesión
    if request.endpoint not in allowed_routes and 'user' not in session:
        if request.endpoint == 'inicio':
            # Redireccionar a la página de inicio de sesión en lugar de la página principal
            return redirect(url_for('login'))
        else:
            # Mostrar página 404 si se accede a una ruta que no existe
            abort(404)

# ruta para iniciar sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # código para procesar el inicio de sesión
        session['user'] = username # guardar información del usuario en sesión
        return redirect(url_for('inicio'))
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # código para procesar el registro del usuario y guardarlo en la base de datos
        session['user'] = username # guardar información del usuario en sesión
        return redirect(url_for('inicio'))
    else:
        return render_template('register.html')

@app.errorhandler(404)
def page_not_found(error):
    return "OCURRIO UN ERROR, NO SE ENCONTRO LA PAGINA (EJEMPLO EXAMEN)", 404

@app.route('/')
@app.route('/index')
def inicio():
    if 'user' in session:
        """
        Función que maneja la ruta de la página principal. 
        Obtiene todos los elementos de la tabla Menu y el número total de menús y los pasa a la plantilla 'index.html' 
        """
        psicologo = Psicologo.query.all()
        totalPsicologos = Psicologo.query.count()
        return render_template('index.html', psicologo = psicologo,totalPsicologos = totalPsicologos)
    else:
       return redirect(url_for('login')) # redirecciona a la página de inicio de sesión
    
@app.route('/Psicologo',methods = ["GET","POST"] )
def agregarpsico():
    if 'user' in session:
        psicologo = Psicologo()  # Crea una nueva instancia del modelo de menú
        psicologoform = psicologoForm(obj=psicologo)  # Instancia un formulario y lo rellena con los datos del menú
        if request.method== "POST":
            if psicologoform.validate_on_submit():  # Valida el formulario
                psicologoform.populate_obj(psicologo)  # Rellena el objeto de menú con los datos del formulario
                db.session.add(psicologo)  # Agrega el objeto de menú a la sesión de la base de datos
                db.session.commit()  # Guarda los cambios en la base de datos
                return redirect(url_for('inicio'))  # Redirige al usuario a la página principal
        return render_template('./Psicologo.html',forma=psicologoform)
    else:
       return redirect(url_for('login')) # redirecciona a la página de inicio de sesión
   
@app.route('/editar/<int:id>',methods = ["GET","POST"])
def editar(id):
    if 'user' in session:
        """
        Función que maneja la ruta para editar un menú existente. 
        Obtiene el menú correspondiente al ID proporcionado, instancia un formulario y valida el formulario. 
        Si el formulario es válido, se actualiza el menú en la base de datos y se redirige al usuario a la página principal. 
        """
        psicologo = Psicologo.query.get_or_404(id)  # Obtiene el menú correspondiente al ID proporcionado o devuelve un error 404 si no existe
        psicologoform = psicologoForm(obj=psicologo)  # Instancia un formulario y lo rellena con los datos del menú
        if request.method== "POST":
            if psicologoform.validate_on_submit():  # Valida el formulario
                psicologoform.populate_obj(psicologo)  # Rellena el objeto de menú con los datos del formulario
                db.session.commit()  # Guarda los cambios en la base de datos
                app.logger.debug(f'psicologo act: {psicologo}')  # Registro de depuración
            return redirect(url_for('inicio'))  # Redirige al usuario a la página principal
        return render_template('./editar.html',forma=psicologoform)
    else:
       return redirect(url_for('login')) # redirecciona a la página de inicio de sesión

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'user' in session:
        """ 
        Función que maneja la ruta para eliminar un menú existente. 
        Obtiene el menú correspondiente al ID proporcionado, lo elimina de la base de datos
        """
        psicologo = Psicologo.query.get_or_404(id)
        db.session.delete(psicologo)
        db.session.commit()
        app.logger.debug(f'dato eliminado: {psicologo}')
        return redirect(url_for('inicio'))
    else:
       return redirect(url_for('login')) # redirecciona a la página de inicio de sesión
    
@app.route('/psicologos/<int:id>', methods=['DELETE'])
def eliminar_psicologo(id):
    psicologo = Psicologo.query.get_or_404(id)
    db.session.delete(psicologo)
    db.session.commit()
    return 'El psicólogo ha sido eliminado', 200

@app.route('/paciente/obtener',methods = ["GET"])
def obtenerpaciente():
    # Obtiene todos los menús de la base de datos
    paciente = Paciente.query.all()
    
    # Crea una lista vacía para almacenar los menús
    listaPaciente = []
    
    # Recorre todos los menús obtenidos de la base de datos y crea un diccionario con sus atributos
    for p in paciente:
        pacienteagg = {}
        pacienteagg["nombre"] = p.nombre
        pacienteagg["telefono"] = p.telefono
        pacienteagg["edad"] = p.edad
        pacienteagg["monto"] = p.monto
        
        # Registra en el archivo de registro el listado de menús
        app.logger.debug(f'listado Menu: {paciente}')
        
        # Agrega el diccionario a la lista de menús
        listaPaciente.append(pacienteagg)
    
    # Retorna una respuesta JSON con la lista de menús
    return jsonify({"status":"OK","mensaje":listaPaciente})
 
@app.route('/empleadohttp/agregar', methods=["POST"])
def agregarEmpleadoHttp():
    try:
        # Obtiene el objeto JSON de la solicitud y crea un objeto Empleado con los datos proporcionados
        json = request.get_json()
        empleado = Empleado()
        empleado.nombre = json['nombre']
        empleado.puesto = json['puesto']
        empleado.sueldo = json['sueldo']
        empleado.correo = json['correo']
        empleado.departamento = json['departamento']
        
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
        empleado.puesto = json['puesto']
        empleado.sueldo = json['sueldo']
        empleado.correo = json['correo']
        empleado.departamento = json['departamento']
        
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
    
@app.route('/sucursalhttp/agregar', methods=["POST"])
def agregarSucursalHttp():
    try:
        # Obtiene el objeto JSON de la solicitud y crea un objeto Empleado con los datos proporcionados
        json = request.get_json()
        sucursal = Sucursal()
        sucursal.nombre = json['nombre']
        sucursal.direccion = json['direccion']
        sucursal.telefono = json['telefono']
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(sucursal)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue agregado a la base de datos
        app.logger.debug(f'sucursal agregado: {sucursal}')
        
        # Retorna una respuesta JSON indicando que el empleado fue agregado exitosamente
        return jsonify({"status":200,"mensaje":"sucursal actualizado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al agregar: {sucursal}')
        return jsonify({"status":400,"mensaje":ex})

# Ruta para editar un empleado en la base de datos
@app.route('/sucursalhttp/editar', methods=["POST"])
def editarSucursalhttp():
    try:
        # Obtiene el objeto JSON de la solicitud y busca el empleado correspondiente en la base de datos por su ID
        json = request.get_json()
        sucursal = Sucursal.query.get_or_404(json["id"])
        
        # Actualiza los atributos del objeto Empleado con los datos proporcionados en el objeto JSON
        json = request.get_json()
        sucursal = Sucursal()
        sucursal.nombre = json['nombre']
        sucursal.direccion = json['direccion']
        sucursal.telefono = json['telefono']
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(sucursal)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue actualizado en la base de datos
        app.logger.debug(f'empleado actualizado: {sucursal}')
        
        # Retorna una respuesta JSON indicando que el empleado fue actualizado exitosamente
        return jsonify({"status":"OK","mensaje":"empleado modificado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al editar: {sucursal}')
        return jsonify({"status":400,"mensaje":ex})


@app.route('/equipo/agregar', methods=["POST"])
def equipoSucursal():
    try:
        # Obtiene el objeto JSON de la solicitud y crea un objeto Empleado con los datos proporcionados
        json = request.get_json()
        equipo = Equipo()
        equipo.nombre = json['nombre']
        equipo.descripcion = json['descripcion']
       
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(equipo)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue agregado a la base de datos
        app.logger.debug(f'equipo agregado: {equipo}')
        
        # Retorna una respuesta JSON indicando que el empleado fue agregado exitosamente
        return jsonify({"status":200,"mensaje":"equipo actualizado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al agregar: {equipo}')
        return jsonify({"status":400,"mensaje":ex})

# Ruta para editar un empleado en la base de datos
@app.route('/equipohttp/editar', methods=["POST"])
def editaEquipohttp():
    try:
        # Obtiene el objeto JSON de la solicitud y busca el empleado correspondiente en la base de datos por su ID
        json = request.get_json()
        equipo = Equipo.query.get_or_404(json["id"])
        
        # Actualiza los atributos del objeto Empleado con los datos proporcionados en el objeto JSON
        json = request.get_json()
        sucursal = Sucursal()
        equipo = Equipo()
        equipo.nombre = json['nombre']
        equipo.descripcion = json['descripcion']
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(equipo)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue actualizado en la base de datos
        app.logger.debug(f'empleado actualizado: {equipo}')
        
        # Retorna una respuesta JSON indicando que el empleado fue actualizado exitosamente
        return jsonify({"status":"OK","mensaje":"equipo modificado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al editar: {equipo}')
        return jsonify({"status":400,"mensaje":ex})

@app.route('/paciente/agregar', methods=["POST"])
def pacienteAgg():
    try:
        # Obtiene el objeto JSON de la solicitud y crea un objeto Empleado con los datos proporcionados
        json = request.get_json()
        paciente = Paciente()
        paciente.nombre = json['nombre']
        paciente.telefono = json['telefono']
        paciente.edad = json['edad']
        paciente.monto = json['monto']
       
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(paciente)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue agregado a la base de datos
        app.logger.debug(f'equipo agregado: {paciente}')
        
        # Retorna una respuesta JSON indicando que el empleado fue agregado exitosamente
        return jsonify({"status":200,"mensaje":"equipo actualizado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al agregar: {paciente}')
        return jsonify({"status":400,"mensaje":ex})

# Ruta para editar un empleado en la base de datos
@app.route('/paciente/editar', methods=["POST"])
def editapacientehttp():
    try:
        # Obtiene el objeto JSON de la solicitud y busca el empleado correspondiente en la base de datos por su ID
        json = request.get_json()
        paciente = Paciente.query.get_or_404(json["id"])
        
        # Actualiza los atributos del objeto Empleado con los datos proporcionados en el objeto JSON
        json = request.get_json()
        paciente = Paciente()
        paciente.nombre = json['nombre']
        paciente.telefono = json['telefono']
        paciente.edad = json['edad']
        paciente.monto = json['monto']
       
       
        
        # Agrega el objeto Empleado a la base de datos y guarda los cambios
        db.session.add(equipo)
        db.session.commit()
        
        # Registra en el archivo de registro que el empleado fue actualizado en la base de datos
        app.logger.debug(f'empleado actualizado: {paciente}')
        
        # Retorna una respuesta JSON indicando que el empleado fue actualizado exitosamente
        return jsonify({"status":"OK","mensaje":"equipo modificado"})
    
    except Exception as ex:
        # Si se produce un error, registra el error en el archivo de registro y retorna una respuesta JSON con el mensaje de error
        app.logger.error(f'error al editar: {equipo}')
        return jsonify({"status":400,"mensaje":ex})
