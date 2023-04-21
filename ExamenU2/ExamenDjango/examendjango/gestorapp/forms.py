from django.forms import ModelForm
from gestorapp.models import Estudiante
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'