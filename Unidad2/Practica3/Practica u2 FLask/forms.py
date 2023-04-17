# Se importan las clases y funciones necesarias de los módulos FlaskForm, StringField, SubmitField y FormField de la extensión flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import FormField

# Se define la clase menuForm que hereda de FlaskForm y tiene tres atributos tipo StringField y un atributo tipo SubmitField
class menuForm(FlaskForm):
    nombreProducto = StringField('Nombre Producto',validators=[DataRequired()])
    Costo = StringField('costo')
    Descripcion = StringField('Descripcion',validators= [DataRequired()])
    enviar = SubmitField('Enviar')

# Se define la clase formularioCompleto que hereda de FlaskForm y tiene un atributo tipo FormField que hace referencia a la clase menuForm
class formularioCompleto(FlaskForm):
    form_menu = FormField(menuForm)

# Se define la clase empleadosForm que hereda de FlaskForm y tiene tres atributos tipo StringField y un atributo tipo SubmitField
class empleadosForm(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired()])
    Puesto = StringField('Puesto')
    Sueldo = StringField('Sueldo',validators= [DataRequired()])
    enviar = SubmitField('Enviar')

# Se define la clase pedidoForm que hereda de FlaskForm y tiene tres atributos tipo StringField y un atributo tipo SubmitField
class pedidoForm(FlaskForm):
    Producto = StringField('Producto',validators=[DataRequired()])
    Costo = StringField('Costo')
    Direccion = StringField('Direccion',validators= [DataRequired()])
    enviar = SubmitField('Enviar')
