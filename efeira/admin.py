from django.contrib import admin
from .models import Produtor, Produto

# Register your models here.
class ProdutorAdmin(admin.ModelAdmin):
    # Personalize as opções do admin, se necessário
    pass

class ProdutoAdmin(admin.ModelAdmin):
    # Personalize as opções do admin, se necessário
    pass

admin.site.register(Produtor, ProdutorAdmin)
admin.site.register(Produto, ProdutorAdmin)