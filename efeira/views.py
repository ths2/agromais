
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Produtor
from .forms import ProdutoForm, ProdutorForm, PesquisaProdutoForm


def pagina_de_boas_vindas(request):
    return render(request, 'pagina_de_boas_vindas.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def pesquisa_produtos(request):
    produtos = []
    termo_de_pesquisa = ''

    if 'termo_de_pesquisa' in request.GET:
        form = PesquisaProdutoForm(request.GET)
        if form.is_valid():
            termo_de_pesquisa = form.cleaned_data['termo_de_pesquisa']
            produtos = Produto.objects.filter(nome__icontains=termo_de_pesquisa)

    else:
        form = PesquisaProdutoForm()

    return render(request, 'pesquisa_produtos.html', {'produtos': produtos, 'form': form, 'termo_de_pesquisa': termo_de_pesquisa})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)  # Inclua request.FILES aqui
        if form.is_valid():
            produtor = Produtor.objects.get(user=request.user)
            produto = form.save(commit=False)
            produto.produtor = produtor
            produto.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redirecione para a lista de produtos após a edição bem-sucedida
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

def cadastrar_produtor(request):
    if request.method == 'POST':
        form = ProdutorForm(request.POST)
        if form.is_valid():
            produtor = form.save(commit=False)
            produtor.user = request.user  # Associe o usuário atual ao produtor
            produtor.save()
            return redirect('alguma_pagina_de_sucesso')  # Redirecione para a página de sucesso após o cadastro
    else:
        form = ProdutorForm()

    return render(request, 'cadastrar_produtor.html', {'form': form})