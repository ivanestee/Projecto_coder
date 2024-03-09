from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Curso
from accounts.forms import CursoFormulario

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')  # Redireccionar a la vista de perfil después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'padre.html')

def curso_form(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        camada = request.POST.get('camada')
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return redirect('inicio')  # Redirige a la página de inicio después de agregar el curso
    return render(request, "accounts/curso_formulario.html")

def cursos(request):
    return render(request, 'accounts/cursos.html')

def inicio(request):
    # Lógica para la página de inicio
    return render(request, 'accounts/ inicio.html')  # Renderiza el template de la página de inicio

def curso_form_2(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():  # Agrega paréntesis aquí
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
            return render(request, "accounts/inicio.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "accounts/cursoFormulario.html", {"formulario": miFormulario})




