# pessoas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('sucesso/', views.sucesso, name='sucesso'),
]