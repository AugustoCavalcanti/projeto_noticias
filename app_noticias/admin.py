from django.contrib import admin
from .models import Noticia, Pessoa, Tag, Categoria

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass