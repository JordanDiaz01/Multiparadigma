from django.forms import ModelForm
from Jugadores.models import Jugadores
class JugadorForm(ModelForm):
    class Meta:
        model = Jugadores
        fields = '__all__'