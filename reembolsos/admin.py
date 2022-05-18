from re import search
from django.contrib import admin
from .models import Reembolso


class ListaReembolsos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'alimentacao', 'combustivel', 'enviado', 'data_cadastro', 'data_servico',
                    'hora_servico', 'memoria_atend', 'rota1', 'rota2', 'rota3', 'rota5', 'rota5')
    list_display_links = ('id', 'nome', 'email')
    list_editable = ('enviado',)
    search_fields = ('nome',)
    list_filter = ('nome',)

    list_per_page = 10


admin.site.register(Reembolso, ListaReembolsos)
