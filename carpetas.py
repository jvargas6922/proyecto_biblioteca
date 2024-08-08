import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from documentos_app.models import Carpeta

#ORM
carpetas = Carpeta.objects.all()
with open('carpetas.txt','w') as f:
    f.write(f'Capetas -------- Documentos \n')
    f.write('*' * 50 + '\n')
    for cap in carpetas:
        f.write(f'{ cap.id_carpeta } - { cap.carpeta } - { cap.id_documento }\n')
    f.write('*' * 50 + '\n')
print('Archivo creado')

