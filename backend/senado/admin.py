from django.contrib import admin
from .models.api import *
from .models.database import *

# Register your models here.

admin.site.register(PesquisaMateriaService)
admin.site.register(Materia)
admin.site.register(Autoria)
