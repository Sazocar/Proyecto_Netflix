from django.contrib import admin
from .models import User, CreditCard, City, Country, Ubication
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ('created', 'updated')
    list_display = ('user_name',)
    readonly_fields = ('id_user',)


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('id_credit_card',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('id_city',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('id_country',)


class UbicationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')


admin.site.register(User, UserAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Ubication, UbicationAdmin)
