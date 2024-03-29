from django.forms.models import BaseInlineFormSet
from django import forms
from .models import Influenciadores, Produto, Variacao, ImagemProduto, Categoria, Fornecedor, ContasPagar, Tipo


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome',)


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ('nome',)


class ContasPagarForm(forms.ModelForm):
    class Meta:
        model = ContasPagar
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }


class VariacaoObrigatoria(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(VariacaoObrigatoria, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ('slug',)


class ImagemProdutoForm(forms.ModelForm):
    imagens = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)

    class Meta:
        model = ImagemProduto
        fields = ['imagem']


class VariacaoForm(forms.ModelForm):
    class Meta:
        model = Variacao
        fields = ['nome', 'preco', 'preco_promocional', 'estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da variação'}),
            'preco': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
            'preco_promocional': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
            'estoque': forms.NumberInput(attrs={'min': 0, 'step': 1}),
        }


class InfluenciadoresForm(forms.ModelForm):
    class Meta:
        model = Influenciadores
        fields = '__all__'
