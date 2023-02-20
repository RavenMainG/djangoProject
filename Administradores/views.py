from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from Login.models import Alumno, Credencial, Solicitud

# def loginAdministrador(request):

#     if request.method == "POST":

#         user = authenticate(username=request.POST.get("email"), password=request.POST.get("password"))

#         if user is not None and not user.is_root():
#             login(request, user)
#             return redirect('panel')

#         else:
#             return render(request, 'Login/login.html')

#     return render(request, 'Login/login.html')

# def panelControl(request):
#     return render(request, 'Login/registroExitosoAdmin.html')


@login_required
def PaneAdministradores(request):
    
    solicitudes = Solicitud.objects.filter(estado_solicitud='pendiente').exists()
    
    if solicitudes:
        solicitudes_pendientes = Solicitud.objects.filter(estado_solicitud='pendiente').select_related('alumno')
        context = {
            'solicitudes': solicitudes_pendientes
        }
        return render(request, 'Administradores/panelAdministrador.html', context)
    else:
        context = {
            
        }
        return render(request, 'Administradores/panelAdministrador.html', context)

    
#Designed by slowcode