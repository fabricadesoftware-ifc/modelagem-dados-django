from django.contrib import admin

from .models import Categoria, Pais, TipoAtuacao, Produtora, Membro, Filme, Atuacao

admin.site.register(Categoria)
admin.site.register(Pais)
admin.site.register(TipoAtuacao)
admin.site.register(Produtora)
admin.site.register(Membro)
admin.site.register(Filme)
admin.site.register(Atuacao)