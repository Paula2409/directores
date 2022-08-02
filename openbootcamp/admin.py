from django.contrib import admin
from openbootcamp.models import Directores

class DirectoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'peliculas')
    
admin.site.register(Directores,DirectoresAdmin)
