from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .forms import LoginForm
from .models import Usuario

# Vista de Login
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')  # Cambia 'inicio' por la vista que quieres mostrar tras login
        else:
            form.add_error(None, 'Usuario o contraseña incorrectos')
        
    return render(request, 'auth_app/login.html', {'form': form})

# Vista Registrar nuevo usuario
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.email = form.cleaned_data['correo']
            cuenta.save()

            usuario = Usuario.objects.create(
                cuenta=cuenta,
                nombre=form.cleaned_data['nombre'],
                apellido_paterno=form.cleaned_data['apellido_paterno'],
                apellido_materno=form.cleaned_data['apellido_materno'],
                genero=form.cleaned_data['genero'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                telefono=form.cleaned_data['telefono'],
            )

            return redirect('login')  # Ajusta según tu URL

    else:
        form = RegistroForm()
    return render(request, 'auth_app/registro.html', {'form': form})

# Menu principal
def inicio_view(request):
    return render(request, 'auth_app/inicio.html')