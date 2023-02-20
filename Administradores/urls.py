from django.urls import path
from . import views

urlpatterns = [
    path('panel_administrador', views.PaneAdministradores, name='panel_administrador'),
]
