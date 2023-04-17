from django.forms import ModelForm
from Historial.models import Historial
class HistorialForm(ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'