from .models import Documento, Carpeta

#metodos documento
def get_documentos():
    #return Documento.objects.all()
    documentos = Documento.objects.all()
    return documentos

def documento(id):
    try:
        documento = Documento.objects.get(id_documento=id)
        return documento
    except Exception as e:
        return e
    

def crear_documento(nombre):
    try:
        documento = Documento(documento=nombre)
        documento.save()
        return documento
    except Exception as e:
        return e

def actualizar_documento(id,nuevo_nombre):
    try:
        doc = documento(id)
        doc.documento = nuevo_nombre
        doc.save()
        return doc
    except Exception as e:
        return e

def eliminar_documento(id):
    try:
        doc = documento(id)
        doc.delete()
        return doc
    except Exception as e:
        return e
    
#metodos carpeta
def get_carpetas():
    return Carpeta.objects.all()

def carpeta(id):
    try:
        carpeta = Carpeta.objects.get(id_carpeta=id)
        return carpeta
    except Exception as e:
        return e
    
def crear_carpeta(nombre,id):
    try:
        doc = documento(id)
        carpeta = Carpeta(carpeta=nombre,id_documento=doc)
        carpeta.save()
        return carpeta
    except Exception as e:
        return e
    
def actualizar_carpeta(id,nueva_carpeta=None,id_documento=None):
    try:
        cap = carpeta(id)
        if nueva_carpeta:
            cap.carpeta = nueva_carpeta
        if id_documento:
            doc = documento(id_documento)
            cap.id_documento = doc
        cap.save()
        return cap
    except Exception as e:
        return e
    
def eliminar_carpeta(id):
    try:
        cap = carpeta(id)
        cap.delete()
        return cap
    except Exception as e:
        return e


