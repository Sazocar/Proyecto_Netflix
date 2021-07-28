from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ('created', 'updated')
    list_display = ('user_name',)
    readonly_fields = ('id_user',)

class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('id_credit_card',)
    
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    readonly_fields = ('id_ciudad',)

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    readonly_fields = ('id_pais',)

admin.site.register(User, UserAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Pais, PaisAdmin)
