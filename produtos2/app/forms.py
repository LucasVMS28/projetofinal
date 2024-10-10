from django import forms
from . models import Produto

class Produtoform(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao']