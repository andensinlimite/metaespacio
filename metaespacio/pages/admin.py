from django.contrib import admin
from . import models


class PaginaAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'espacio', 'orden', 'menu']
    list_filter = ['espacio']

admin.site.register(models.Pagina, PaginaAdmin)
