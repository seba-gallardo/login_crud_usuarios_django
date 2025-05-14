from django.shortcuts import render, get_object_or_404, redirect
from auth_app.models import Usuario
from auth_app.forms import RegistroForm
from .forms import UsuarioEditForm

# Listar usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'crudSeba/listar_usuarios.html', {'usuarios': usuarios})

# Vista Registrar nuevo usuario
def crear_usuario(request):
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

            return redirect('listar_usuarios')  # Ajusta según tu URL

    else:
        form = RegistroForm()
    return render(request, 'crudSeba/registro_usuario.html', {'form': form})

# Editar usuario
def editar_usuario(request, cuenta_id):
    usuario = get_object_or_404(Usuario, cuenta_id=cuenta_id)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'crudSeba/editar_usuario.html', {'form': form, 'usuario': usuario})

# Eliminar usuario
def eliminar_usuario(request, cuenta_id):
    usuario = get_object_or_404(Usuario, cuenta_id=cuenta_id)
    if request.method == 'POST':
        usuario.cuenta.delete()  # También elimina el Usuario porque es OneToOne con CASCADE
        return redirect('listar_usuarios')
    return redirect('listar_usuarios')


