from django.forms import ModelForm
from contratos.models import Contratos
class ContratoForm(ModelForm):
    class Meta:
        model = Contratos
        fields = '__all__'