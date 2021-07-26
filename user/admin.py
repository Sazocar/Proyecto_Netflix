from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ('created', 'updated')
    list_display = ('email',)

admin.site.register(User, UserAdmin)