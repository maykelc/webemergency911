from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Alerta
from .forms import UsuarioForm, AlertaForm
from django.contrib.auth import logout


def base(request):
    return render(request, 'base.html')


def inicio(request):
    # Obtener todas las alertas
    alertas = Alerta.objects.all()
    # Verificar si hay un usuario autenticado
    usuario_autenticado = request.session.get('usuario_id') is not None
    return render(request, 'inicio.html', {'alertas': alertas, 'usuario_autenticado': usuario_autenticado})


def login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            correo = request.POST.get('correo')
            contrasena = request.POST.get('contrasena')
            try:
                usuario = Usuario.objects.get(
                    correo=correo, contrasena=contrasena)
                request.session['usuario_id'] = usuario.id
                return redirect('inicio')
            except Usuario.DoesNotExist:
                error_login = 'Credenciales incorrectas'
                form = UsuarioForm()
                return render(request, 'login.html', {'error_login': error_login, 'form': form})

        elif 'register' in request.POST:
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('inicio')
            else:
                error_register = 'Error en el registro. Verifica los datos ingresados.'
                return render(request, 'login.html', {'error_register': error_register, 'form': form})

    form = UsuarioForm()
    return render(request, 'login.html', {'form': form})


def create_alert(request):
    if request.method == 'POST':
        form = AlertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirigir a la página de inicio
    else:
        form = AlertaForm()

    return render(request, 'create.html', {'form': form})


def contacto(request):
    return render(request, 'contacto.html')


def sobremi(request):
    return render(request, 'sobremi.html')


def servicio(request):
    return render(request, 'servicios.html')


def clima(request):
    return render(request, 'clima.html')


def emergencia_noticia(request):
    return render(request, 'emergencia_noticia.html')


def sismos(request):
    return render(request, 'sismos.html')



def logout_view(request):
    logout(request)
    return redirect('inicio')  # Reemplaza 'inicio' con la URL a la que quieres redirigir luego del logout