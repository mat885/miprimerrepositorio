from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def calcular(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'mensaje': 'Hace falta iniciar sesión.'})
    return redirect('preguntas')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmar = request.POST['confirmar']
        if password == confirmar:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return render(request, 'registro.html')

def preguntas_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        respuestas = [int(request.POST.get(f'p{i}', 0)) for i in range(1, 6)]
        resultado = sum(respuestas) * 2  # ejemplo de cálculo
        return render(request, 'resultado.html', {
            'usuario': request.user.username,
            'resultado': resultado
        })
    return render(request, 'preguntas.html')
