from django.forms import ModelForm
from Empleados.models import Empleado
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'