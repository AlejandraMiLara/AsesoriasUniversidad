from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('salir/', views.salir, name='salir'),
    path('panel/', views.panel, name='panel'),
    #path('mis_materias/', views.mis_materias, name='mismaterias'),
    #path('mis_asesorias/', views.mis_asesorias, name='misasesorias'),
    path('agregar_asesoria/', views.agregar_asesoria, name='agregarasesoria'),
    path('ver_asesorias/', views.ver_asesorias, name='verasesorias'),
    path('editar_asesoria/<int:pk>/', views.editar_asesoria, name='editarasesoria'),
    path('eliminar_asesoria/<int:pk>/', views.eliminar_asesoria, name='eliminarasesoria'),
]
