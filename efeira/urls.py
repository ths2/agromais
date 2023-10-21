from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_de_boas_vindas, name=''),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('cadastrar_produtor/', views.cadastrar_produtor, name='cadastrar_produtor'),
    path('pesquisa/', views.pesquisa_produtos, name='pesquisa_produtos'),

    # Adicione outras URLs aqui
]
