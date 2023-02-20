from django.urls import path
from . import views


urlpatterns = [
    path('panel/', views.Panel, name='panel_alumnos'),
    path('datos/', views.cuenta, name='cuenta_alumnos'),
    path('solicitud/', views.SolicitudAlumno, name='solicitud'),
]
