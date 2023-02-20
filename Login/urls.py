from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('alumnos/crear_cuenta', views.registroAlumno, name='crear_cuenta'),
    path('alumnos/login/', views.LoginAlumnos, name='login_alumnos'),
    path('alumnos/panel/logout/', views.logoutAlumno, name='logout_alumnos'),
    path('alumnos/registro_exitoso', views.RegistroExitoso, name='registro_exitoso'),
    path('alumnos/', include('Alumnos.urls')),
    path('administradores/', include('Administradores.urls')),
    path('administradores/login/', views.LoginAdministrador, name='login_administradores'),
]