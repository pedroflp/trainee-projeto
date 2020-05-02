from django.contrib import admin
from .models import Especialidade, Consulta, QuemSomos

# Register your models here.

admin.site.register(Especialidade)
admin.site.register(Consulta)
admin.site.register(QuemSomos)