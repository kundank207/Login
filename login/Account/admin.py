from django.contrib import admin
from .models import Signup
class SignupAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    
admin.site.register(Signup, SignupAdmin)
