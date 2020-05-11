from django.contrib import admin
from .models import Especialidade, Consulta, QuemSomos


def consulta_respondida(modeladmin, request, queryset):
    queryset.update(respondida=True)
consulta_respondida.short_description = "Marcar como respondida"

def consulta_em_espera(modeladmin, request, queryset):
    queryset.update(respondida=False)
consulta_em_espera.short_description = "Marcar como em espera"

class ConsultaAdmin(admin.ModelAdmin):
    actions = [consulta_respondida, consulta_em_espera]

# Register your models here.

admin.site.register(Especialidade)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(QuemSomos)