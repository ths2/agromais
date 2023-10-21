from django import forms
from .models import Produto, Produtor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria', 'imagem', 'data_inicio_colheita', 'data_fim_colheita', 'pronto_para_colheita']
        widgets = {
            'data_inicio_colheita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim_colheita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
class ProdutorForm(forms.ModelForm):
    class Meta:
        model = Produtor
        fields = ['nome', 'localizacao', 'contato']

class PesquisaProdutoForm(forms.Form):
    termo_de_pesquisa = forms.CharField(label='Pesquisar Produto', max_length=100)