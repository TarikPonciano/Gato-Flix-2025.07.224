from django.urls import path
# from . import views
from .views import home, login_view, cadastro

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('cadastro/', cadastro, name='cadastro'),
]