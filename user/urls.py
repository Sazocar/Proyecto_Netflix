from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name="user"),
    path('suscription_2', views.suscription_2, name="suscription_2"),
]
