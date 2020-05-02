from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('especialidades/<int:id>/', views.especialidade_especifica, name='especialidade_especifica'),
    path('confirmacao/<str:nome>/', views.confirmacao_consulta, name='confirmacao_consulta'),
]