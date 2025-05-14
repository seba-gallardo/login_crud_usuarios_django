from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:cuenta_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:cuenta_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
