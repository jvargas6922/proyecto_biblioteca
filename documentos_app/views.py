from django.shortcuts import render
from django.http import HttpResponse
from .forms import CrearDocumentoForm, CrearCarpetaForm

# Create your views here.
def index_documentos_app(request):
    #form = CrearDocumentoForm()
    form = CrearCarpetaForm()
    return render(request, 'documentos_app/index.html',{'form':form})
