"""djangopapa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.index, name = 'index'),
    path('helloworld/',myapp.views.Hola_mundo, name = 'hello-world'),
    path('index/',myapp.views.index,name = 'index'),
    path('articulos/',myapp.views.articulos,name = 'articulos'),
    path('años/',myapp.views.años,name = 'años'),
    path('contacto/',myapp.views.contacto, name = 'contacto'),
    path('contacto/<str:nombre>/',myapp.views.contacto, name = 'contacto'),
    path('contacto/<str:nombre>/<str:apellido>',myapp.views.contacto, name = 'contacto'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',myapp.views.CrearArticulo, name = 'crear-articulo'),
    path('articulo/', myapp.views.Articulo, name='articulo'),
    path('Editar-articulo/<str:id>',myapp.views.EditarArticulo, name='Editar-articulo'),
    path('eliminar/<int:id>',myapp.views.EliminarArticulos, name='eliminar'),
    path('save-article',myapp.views.SaveArticulo, name='save'), 
    path('Create-article/',myapp.views.create_article,name = 'create'),
    path('create-full-article',myapp.views.create_full_article, name = 'create_full')


]
