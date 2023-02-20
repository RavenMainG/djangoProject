import email

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Credencial, Alumno
from .forms import AlumnoFormulario


def Home(request):
    return render(request, 'Login/home.html')


def logoutAlumno(request):
    print('esto antes de deslog')

    logout(request)

    print('esto despues del deslog')
    return redirect('login_alumnos')


def LoginAlumnos(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_alumno:
            login(request, user)
            return redirect('panel_alumnos')
        else:
            context = {
                'error': 'Correo o contraseña inválidos.'
            }
            return render(request, 'Login/loginAlumno.html', context)
    else:
        context = {}
        return render(request, 'Login/loginAlumno.html', context)


def RegistroExitoso(request):
    return render(request, 'Login/registroExitoso.html')


def registroAlumno(request):
    if request.method == 'POST':
        form = AlumnoFormulario(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            print(email)
            alumno = Alumno.objects.get(email = email)
            print(alumno)
            credencial = Credencial(estado_credencial='inactiva', alumno=alumno)
            credencial.save()
            return redirect('registro_exitoso')
        else:
            return render(request, 'Login/registroAalumno.html', {'form': form})

    else:
        form = AlumnoFormulario()
        context = {
            'form': form
        }
        return render(request, 'Login/registroAalumno.html', context)

def logoutAdministrador(request):
    print('esto antes de deslog')

    logout(request)

    print('esto despues del deslog')
    return redirect('login_administradores')

def LoginAdministrador(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None and user.is_staff:
            print('si es administrador')
            login(request, user)
            return redirect('panel_administrador')
        else:
            print('no es administrador')
            context = {
                'error': 'Correo o contraseña inválidos.'
            }
            return render(request, 'Login/loginAdministrador.html', context)
    else:
        context = {}
        return render(request, 'Login/loginAdministrador.html', context)