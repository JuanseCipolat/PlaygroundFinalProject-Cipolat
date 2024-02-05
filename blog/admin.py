from django.contrib import admin
from .models import Publicacion

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    search_fields = ('titulo', 'autor__username')  

admin.site.register(Publicacion, PublicacionAdmin)