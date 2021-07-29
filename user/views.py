from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from user.forms import UserModelForm, CreditCardModelForm, UbicationModelForm
from .models import User, CreditCard, Ubication, City, Country
from django.http import JsonResponse

# Create your views here.


def select_genero(request):
    return render(request, "user/select_genero.html")

def ubication_create_view(request):
    ubication_form = UbicationModelForm()
    if request.method == 'POST':
        ubication_form = UbicationModelForm(request.POST)
        if ubication_form.is_valid():
            ubication_form.save()
            current_user = request.user
            print(current_user)
            return redirect("select_genero")
    return render(request, 'user/suscription_2.html', {'ubication_form': ubication_form})


def ubication_update_view(request, pk):
    ubication = get_object_or_404(Ubication, pk=pk)
    ubication_form = UbicationModelForm(instance=ubication)
    if request.method == 'POST':
        ubication_form = UbicationModelForm(request.POST, instance=ubication)
        if ubication_form.is_valid():
            ubication_form.save()
            return redirect('select-genero', pk=pk)
    return render(request, 'user/suscription_2.html', {'ubication_form': ubication_form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    # print(list(cities.values('country_id', 'name')))
    return render(request, 'user/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('country_id', 'name')), safe=False)

# def suscription_2(request, *args, **kwargs):
#     ubicacion_form = UserModelForm(request.POST or None)
#     if request.method =="POST" and ubicacion_form.is_valid():
#         data_user = ubicacion_form.cleaned_data
#         Ubicacion.objects.create(**data_user)
#         ubicacion_form = UserModelForm()
#     return render(request, "user/suscription_2.html", {'ubicacion_form': ubicacion_form})


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
        return redirect("suscription_2")
    # user_form = UserModelForm(request.POST) # Se crea una plantilla vacia
    # if request.method == "POST":  # Se detecta si se ha enviado por POST algun dato
    #     user_form = UserModelForm(request.POST)   # Y si se envio algun dato se rellena con esta información
    #     if user_form.is_valid():
    #         user_form.save()
    #         # obj = user_form.save(commit=True)
    #         # Do some stuff
    #         # obj.save()
    #         # Suponemos que todo esta OK, redireccionamos
    return render(request, "user/suscription_1.html", {'user_form': user_form,
                                                       'card_form': credit_card_form})
