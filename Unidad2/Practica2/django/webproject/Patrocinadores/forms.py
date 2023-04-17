from django.forms import ModelForm
from Patrocinadores.models import Patrocinadores
class PatrocinadorForm(ModelForm):
    class Meta:
        model = Patrocinadores
        fields = '__all__'