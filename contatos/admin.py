from django.contrib import admin
from .models import Categoria,Contato



# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    # campos que irá aparecer na tela admin
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao','categoria','mostrar')
    #campos linkados que ao clicar irá abrir o usuário
    list_display_links = ('id','nome','sobrenome')
    #adicionando campos para filtrar
    list_filter = ('nome','sobrenome')
    #numero de paginas a apresentar por pagina
    list_per_page = 10
    #campos de busca, que irá buscar pelos atributos abaixo
    search_fields = ('nome','sobrenome','telefone')

    list_editable= ('telefone','mostrar')







admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)