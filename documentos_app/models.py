from django.db import models

# Create your models here.
class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'documentos'

    def __str__(self):
        return self.documento
    
class Carpeta(models.Model):
    id_carpeta = models.AutoField(primary_key=True)
    carpeta = models.CharField(max_length=100)
    id_documento = models.ForeignKey(Documento, on_delete=models.CASCADE, db_column='id_documento')

    class Meta:
        managed = False
        db_table = 'carpetas'

    def __str__(self):
        return self.carpeta


    