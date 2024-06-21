"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emergency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login, name="login"),
    path('', views.inicio, name="inicio"),
    path('contacto/',views.contacto, name="contacto"),
    path('crear/',views.create_alert, name="crear"),
    path('nosotros/',views.sobremi, name="nosotros"),
    path('servicios/', views.servicio, name="servicio"),
    path('sismos/',views.sismos, name="sismos"),
    path('clima/',views.clima, name="clima"),
    path('noticias/',views.emergencia_noticia, name="emergencia_noticia"),
    path('logout/', views.logout_view, name='logout'),
]
