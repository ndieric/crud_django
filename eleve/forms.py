from django.forms import ModelForm
from .models import Eleve



class EleveForm(ModelForm):
    class Meta:
        model=Eleve
        fields='__all__'