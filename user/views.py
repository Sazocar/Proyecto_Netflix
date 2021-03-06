from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from user.forms import UserModelForm, CreditCardModelForm, UbicationModelForm, PerfilModelForm
from .models import User, CreditCard, Ubication, City, Country, Perfil
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def select_genero(request):
    return render(request, "user/select_genero.html")


def agregar_perfil(request):
    return render(request, "user/agregar_perfiles.html")


def plan(request):
    ubication_form = UbicationModelForm()
    if request.method == 'POST':
        ubication_form = UbicationModelForm(request.POST)
        if ubication_form.is_valid():
            ubication_form.save()
            current_user = request.user
            print(current_user)
            return redirect("agregar-perfil/")
    return render(request, 'user/suscription_2.html', {'ubication_form': ubication_form})

# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    # print(list(cities.values('country_id', 'name')))
    return render(request, 'user/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('country_id', 'name')), safe=False)

def registration(request, *args, **kwargs):
    user_form = UserModelForm(request.POST or None)
    credit_card_form = CreditCardModelForm(request.POST or None)
    if request.method == "POST" and user_form.is_valid() and credit_card_form.is_valid():
        data_user = user_form.cleaned_data
        data_credit_card = credit_card_form.cleaned_data
        User.objects.create(**data_user)
        CreditCard.objects.create(**data_credit_card)
        user_form = UserModelForm()
        credit_card_form = CreditCardModelForm()
        return redirect("plan/")
    return render(request, "user/suscription_1.html", {'user_form': user_form,
                                                       'card_form': credit_card_form})

def add_perfiles(request, *args, **kwargs):
    perfil_form = PerfilModelForm(request.POST or None)
    if request.method == "POST" and perfil_form.is_valid():
        data_perfil = perfil_form.cleaned_data
        Perfil.objects.create(**data_perfil)
        perfil_form = PerfilModelForm()
        return redirect("select-genero/")
    return render(request, "user/agregar_perfiles.html", {'perfil_form': perfil_form})
