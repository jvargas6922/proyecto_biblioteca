from django import forms
from .models import Documento, Carpeta

class CrearDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['documento']

class CrearCarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = ['carpeta','id_documento']