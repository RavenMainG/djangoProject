from django.contrib import admin
from . import  models

admin.site.register(models.Alumno)
admin.site.register(models.Administrador)
admin.site.register(models.Cuatrimestre)
admin.site.register(models.Carrera)
admin.site.register(models.Credencial)
admin.site.register(models.Solicitud)
admin.site.register(models.User)

