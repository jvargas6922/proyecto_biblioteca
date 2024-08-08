from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_documentos_app, name='index_documentos_app'),
]