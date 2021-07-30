from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.registration, name="registration"),
    path('plan/', views.plan, name="plan"),
    path('plan/agregar-perfil/', views.add_perfiles, name="agregar-perfil"),
    path('plan/agregar-perfil/select-genero/', views.select_genero, name="select-genero"),
    path('home/', views.home, name="home"),
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
    # path('', RedirectView.as_view(url='<core/>', permanent=False), name='index'),
]
