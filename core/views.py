from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")

def suscripcion_1(request):
    return render(request, "core/suscripcion_1.html")

def suscripcion_2(request):
    return render(request, "core/suscripcion_2.html")

# def select_genero(request):
#     return render(request, "user/select_genero.html")

def agregar_perfil(request):
    return render(request, "core/agregar_perfiles.html")