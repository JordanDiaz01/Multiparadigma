from django.forms import ModelForm,EmailInput
from juegos.models import Juego

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'
        widgets = {
            'email': EmailInput(
            attrs={
            'type':'email',
            'class':'form control',
            'style':'max-width:100px',
            'placeholder':'Correo'
            }
            )
        }