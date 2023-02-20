from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from Login.models import Alumno, Credencial, Solicitud
import Login.models


# Create your views here.
@login_required(redirect_field_name='login_alumnos')
@user_passes_test(lambda u: u.is_alumno, login_url='login_administradores')
def Panel(request):
    if request.user.is_alumno:
        alumno = Alumno.objects.get(email=request.user)
        context = {
            'alumno': alumno
        }
        return render(request, 'Alumnos/panelAlumno.html', context)
    else:
        return redirect('home')
    


@login_required(redirect_field_name='login_alumnos')
def cuenta(request):
    if request.user.is_alumno:
        alumno = Alumno.objects.get(email=request.user)
        context = {
            'alumno': alumno
        }
        return render(request, 'Alumnos/cuenta.html', context)


def SolicitudAlumno(request):
    if request.method == 'POST':
        alumno = Alumno.objects.get(email=request.user)
        solicitud = Solicitud(alumno=alumno, estado_solicitud='pendiente')
        solicitud.save()
        return redirect('panel_alumnos')
    else:
        alumno = Alumno.objects.get(email=request.user)

        credencial = Credencial.objects.get(alumno=alumno)
        solicitud_pendiente = Solicitud.objects.filter(alumno=alumno, estado_solicitud='pendiente').exists()
        solicitud_aprobada = Solicitud.objects.filter(alumno=alumno, estado_solicitud='aprobada').exists()


        if solicitud_pendiente:
            context = {
                'alumno': alumno,
                'solicitud_pendiente': 'pendiente',
            }
        elif solicitud_aprobada:
            context = {
                'alumno': alumno,
                'solicitud_aprobada': 'aprobada',
            }
        else:
            context = {
                'alumno': alumno,
                'solicitud_permiso': 'permiso'
            }

        return render(request, 'Alumnos/solicitud.html', context)
