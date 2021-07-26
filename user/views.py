from django.shortcuts import render, HttpResponseRedirect, redirect
from user.forms import UserModelForm
from .models import User

# Create your views here.
def suscription_2(request):
    return render(request, "user/suscription_2.html")

def user(request, *args, **kwargs):
    user_form = UserModelForm(request.POST or None)
    if user_form.is_valid():
        data = user_form.cleaned_data
        User.objects.create(**data)
        user_form = UserModelForm()
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
    return render(request, "user/suscription_1.html", {'form':user_form})