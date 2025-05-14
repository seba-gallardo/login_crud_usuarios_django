from django import forms
from .models import Cuenta
from django.contrib.auth.forms import UserCreationForm

# Formulario Login
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150, error_messages={'required': 'Por favor ingresa tu nombre de usuario.'})
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, error_messages={'required': 'Por favor ingresa tu contraseña.'})   

# Formulario Crear Nuevo Usuario
class RegistroForm(UserCreationForm):
    correo = forms.EmailField(label='Correo', error_messages={'required': 'Este campo es obligatorio.'})
    nombre = forms.CharField(error_messages={'required': 'Por favor ingresa tu nombre.'})
    apellido_paterno = forms.CharField(error_messages={'required': 'Por favor ingresa tu apellido paterno.'})
    apellido_materno = forms.CharField(error_messages={'required': 'Por favor ingresa tu apellido materno.'})
    genero = forms.ChoiceField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')])
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), error_messages={'required': 'Por favor ingresa tu fecha de nacimiento.'})
    telefono = forms.CharField(error_messages={'required': 'Por favor ingresa tu número de teléfono.'})

    class Meta:
        model = Cuenta
        fields = ['username', 'correo', 'password1', 'password2', 'nombre', 'apellido_paterno', 'apellido_materno', 'genero', 'fecha_nacimiento', 'telefono']
        
        # Personalización de los mensajes de error de los campos de contraseña
        error_messages = {
            'password1': {
                'required': 'Por favor ingresa una contraseña.',
            },
            'password2': {
                'required': 'Por favor confirma tu contraseña.',
                'password_mismatch': 'Las contraseñas no coinciden.',
            },
        }


'''
# Formulario Login
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)   

# Formulario Crear Nuevo Usuario
class RegistroForm(UserCreationForm):
    correo = forms.EmailField(label='Correo')
    nombre = forms.CharField()
    apellido_paterno = forms.CharField()
    apellido_materno = forms.CharField()
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField()

    class Meta: 
        model = Cuenta
        fields = ['username', 'correo', 'password1', 'password2', 'nombre', 'apellido_paterno', 'apellido_materno', 'genero', 'fecha_nacimiento', 'telefono']
        # password1: es donde el usuario escribe la contraseña.
        # password2: es para confirmar que escribió la contraseña correctamente.
        # Django luego valida automáticamente que ambas coincidan usando el método clean() del UserCreationForm.
'''