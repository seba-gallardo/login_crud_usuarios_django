from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]