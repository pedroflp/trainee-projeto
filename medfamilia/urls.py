from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('especialidades/id/', views.especialidade_especifica, name='especialidade_especifica'),
]