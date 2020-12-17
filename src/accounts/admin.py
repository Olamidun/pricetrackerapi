from django.contrib import admin
from accounts.models import Auth
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AuthAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone_number', 'date_joined']
    search_fields = ['email', 'username', 'phone_number']
    readonly_fields = ['date_joined', 'last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Auth, AuthAdmin)