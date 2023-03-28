from flask import Flask,render_template,url_for,redirect,request,jsonify
from flask_migrate import Migrate
from database import db
from models import Persona,Producto
from forms import PersonaForm
import logging
app = Flask(__name__)


USER_DB = 'postgres'
PASS_DB = '1234'
URL_DB = 'localhost'
NAME_DB = 'flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False


db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)

app.config["SECRET_KEY"] = "llave secreta"
@app.route('/')
@app.route('/index')
def inicio():
    personas = Persona.query.all()
    totalpersonas = Persona.query.count()
    app.logger.debug(f'listado de personas: {personas}')
    return render_template('index.html',personas=personas,totalpersonas=totalpersonas)

@app.route('/agregar',methods = ["GET","POST"])
def agregar():
    persona = Persona()
    personaform = PersonaForm(obj=persona)
    if request.method== "POST":
        if personaform.validate_on_submit():
            personaform.populate_obj(persona)
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html',forma=personaform)

@app.route('/editar/<int:id>',methods = ["GET","POST"])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaform =PersonaForm(obj=persona)
    if request.method== "POST":
            if personaform.validate_on_submit():
                personaform.populate_obj(persona)
                db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma=personaform)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/producto/agregar',methods = ["POST"])
def agregarPersona():
     try:
          
            json = request.get_json()
            producto = Producto()
            producto.nombre = json['nombre']
            producto.descripcion = json['descripcion']
            producto.precio = json['precio']
            db.session.add(producto)
            db.session.commit()
            return jsonify({"status":200,"mensaje":"Producto agregado"})
     except Exception as ex:
          return jsonify({"status":400,"mensaje":ex})

@app.route('/producto/editar',methods = ["POST"])
def editarProducto():
     try:
          json = request.get_json()
          producto  = Producto.query.get_or_404(json["id"])
          producto.nombre = json['nombre']
          producto.descripcion = json['descripcion']
          producto.precio = json['precio']
          db.session.commit()
          return jsonify({"status":"OK","mensaje":"Producto modificado"})
     except Exception as ex:
          return jsonify({"status":400,"mensaje":ex})


@app.route('/producto/eliminar',methods = ["POST"])
def elimnarProducto():
     try:
          json = request.get_json()
          producto = Producto.query.get_or_404(json["id"])
          db.session.delete(producto)
          db.session.commit()
          return jsonify({"status":"OK","mensaje":"Producto eliminado"})
     except Exception as ex:
          return jsonify({"status":400,"mensaje":ex})
     

@app.route('/producto/obtener',methods = ["GET"])
def obtenerProducto():
     productos = Producto.query.all()
     litaProductos = []
     for p in productos:
          producto = {}
          producto["nombre"] = p.nombre
          producto["precio"] = p.precio
          producto["descripcion"] = p.descripcion
          litaProductos.append(producto)
     return jsonify({"status":"OK","mensaje":litaProductos})