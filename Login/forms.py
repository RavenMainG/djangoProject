from django import forms
from django.contrib.auth.forms import UserCreationForm
from Login.models import Alumno, Carrera, Cuatrimestre


class AlumnoFormulario(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden.',
    }

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}))
    nombre = forms.CharField(required=True, max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(required=True, max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    matricula = forms.CharField(required=True, max_length=10,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricula'}))
    carrera = forms.ModelChoiceField(required=True, queryset=Carrera.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Carrera'}))
    cuatrimestre = forms.ModelChoiceField(required=True, queryset=Cuatrimestre.objects.all(), widget=forms.Select(
        attrs={'class': 'form-select', 'placeholder': 'Cuatrimestre'}))
    numero_telefono = forms.CharField(required=True, max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Numero de teléfono'}))
    fecha_nacimiento = forms.DateField(required=True,
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    password1 = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(required=True, label='Confirmar contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = Alumno
        fields = (
            'email', 'nombre', 'apellido', 'matricula', 'carrera', 'cuatrimestre', 'numero_telefono',
            'fecha_nacimiento',
            'password1', 'password2')
