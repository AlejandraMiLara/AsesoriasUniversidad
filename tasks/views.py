from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, AgregarAsesoriaForm
from .models import CustomUser, Asesoria

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': CustomUserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    matricula=request.POST['matricula'],
                    role=request.POST['role']
                )
                user.save()
                login(request, user)
                return redirect('panel')
            except:
                return render(request, 'registro.html', {
                    'form': CustomUserCreationForm(),
                    'msj': 'El nombre de usuario ya existe'
                })
        else:
            return render(request, 'registro.html', {
                'form': CustomUserCreationForm(),
                'msj': 'Los passwords no son iguales'
            })

def ingreso(request):
    if request.method == 'GET':
        return render(request, 'ingreso.html', {
            'form': CustomAuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingreso.html', {
                'form': CustomAuthenticationForm,
                'msj': 'Usuario o password incorrecto'
            })
        else:
            login(request, user)
            return redirect('panel')

def salir(request):
    logout(request)
    return redirect('ingreso')

def panel(request):
    return render(request, 'panel.html')

def mis_materias(request):
    return render(request, 'mis_materias.html')

def mis_asesorias(request):
    return render(request, 'mis_asesorias.html')

def agregar_asesoria(request):
    if request.method == 'POST':
        form = AgregarAsesoriaForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('verasesorias')
    else:
        form = AgregarAsesoriaForm(user=request.user)
    return render(request, 'agregar_asesoria.html', {'form': form})

def ver_asesorias(request):
    asesorias = Asesoria.objects.all()
    return render(request, 'ver_asesorias.html', {'asesorias': asesorias})

def editar_asesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, pk=pk)
    if request.method == 'POST':
        form = AgregarAsesoriaForm(request.POST, instance=asesoria, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('verasesorias')
    else:
        form = AgregarAsesoriaForm(instance=asesoria, user=request.user)
    return render(request, 'editar_asesoria.html', {'form': form})

def eliminar_asesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, pk=pk)
    if request.method == 'POST':
        asesoria.delete()
        return redirect('verasesorias')
    return render(request, 'eliminar_asesoria.html', {'asesoria': asesoria})
