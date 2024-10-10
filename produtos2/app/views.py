from django.shortcuts import render, redirect
from .models import Produto
from .forms import Produtoform
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos':produtos})
@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = Produtoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = Produtoform()
    return render(request, 'cadastro.html', {'form': form})
@login_required
def busca(request):
    if 'nome' in request.POST:
        nome = request.POST['nome']
        produtos = Produto.objects.filter(nome__icontains=nome)
        return render(request, 'buscar.html', {'produtos': produtos})
    else:
       produtos = Produto.objects.all()
    return render(request, 'buscar.html', {'produtos': produtos})
@login_required
def excluir(request, id):
    Produtos = Produto.objects.get(id=id)
    Produtos.delete()
    return redirect(home)

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = Produtoform
    template_name = 'cadastro.html'
    success_url = 'http://127.0.0.1:8000/'  # Redireciona após a atualização bem-sucedida

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'hide_menu': True})

def logout_view(request):
    logout(request)
    return redirect('login')
