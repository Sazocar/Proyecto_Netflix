from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name="registration"),
    path('add/', views.ubication_create_view, name="ubication_add"),
    path('<int:pk>/', views.ubication_update_view, name='ubication_change'),
    
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]
