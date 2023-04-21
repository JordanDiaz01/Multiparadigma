from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import FormField

class psicologoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    correo = StringField('Correo')
    sueldo = StringField('Sueldo')
    enviar = SubmitField('Enviar')

