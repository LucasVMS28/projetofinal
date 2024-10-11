from django import forms
from . models import Produto, Usuario

class Produtoform(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']