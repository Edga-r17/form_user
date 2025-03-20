from django.contrib import admin
from users.models.users import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'age',
        'created',
    ]

admin.site.register(User, UserAdmin)
