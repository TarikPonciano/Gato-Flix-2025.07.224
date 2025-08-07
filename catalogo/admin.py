from django.contrib import admin
from .models import Perfil, Filme
# Register your models here.

#Para criar usuário admin, rodar o comando no terminal python manage.py createsuperuser 
admin.site.register(Perfil)
admin.site.register(Filme)