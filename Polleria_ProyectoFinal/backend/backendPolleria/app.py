from flask import Flask
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
import logging
from models import *
from routes.empleados.empleados import appempleado
from routes.sucursales.sucursal import appsucursal
from routes.calif_comentarios.calif_comentarios import appCC
from routes.pedidos.pedidos import apppedido
from routes.historiales.historiales import appHistorial
from routes.menus.menus import appmenu
app = Flask(__name__)

app.register_blueprint(appempleado)
app.register_blueprint(appsucursal)
app.register_blueprint(appCC)
app.register_blueprint(apppedido)
app.register_blueprint(appHistorial)
app.register_blueprint(appmenu)

app.config.from_object(BasicConfig)
CORS(app)
# Inicialización de la base de datos y migración
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)

# Configuración del registro de errores
logging.basicConfig(filename='app.log', level=logging.DEBUG)
