import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from documentos_app.models import Documento

#ORM
#documentos = Documento.objects.all()
#with open('documentos.txt','w') as f:
#    f.write('Documentos\n')
#    f.write('*' * 20 + '\n')
#    for doc in documentos:
#        f.write(f'{doc.id_documento} - {doc.documento}\n')
#    f.write('*' * 20 + '\n')
#print('Archivo creado')

#SQL
documentos = Documento.objects.raw('SELECT * FROM documentos')
with open('documentos.txt','w') as f:
    f.write('Documentos\n')
    f.write('*' * 20 + '\n')
    for doc in documentos:
        f.write(f'{doc.id_documento} - {doc.documento}\n')
    f.write('*' * 20 + '\n')
print('Archivo creado')