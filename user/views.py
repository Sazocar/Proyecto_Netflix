from django.shortcuts import render, HttpResponseRedirect, redirect
from user.forms import UserModelForm, CreditCardModelForm
from .models import User, CreditCard

# Create your views here.
def suscription_2(request):
    return render(request, "user/suscription_2.html")


def registration(request, *args, **kwargs):
    user_form = UserModelForm(request.POST or None)
    credit_card_form = CreditCardModelForm(request.POST or None)
    if request.method =="POST" and user_form.is_valid() and credit_card_form.is_valid():
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
    return render(request, "user/suscription_1.html", {'user_form':user_form,
                                                       'card_form': credit_card_form})
