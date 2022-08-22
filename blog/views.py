from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Post

# Criando view de loginForm com formulário padrão de usuários do django
def loginForm(request):
    form = AuthenticationForm
    return render(request, 'login.html', {'form':form})

#Criando view de autenticação e login
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.error(request, message='Login ou senha inválidos! Tente novamente.')
        return redirect('/loginForm/', {'messages': messages})

#View de logout
def logoutUser(request):
    logout(request)
    return redirect('/')

#View de Blog
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

#Formulário de Criação do Blog
@login_required(login_url='/loginForm/loginUser/')
def add_post(request):
    return render(request, 'add_post.html')

#Salvando postagem no banco
@login_required(login_url='/loginForm/loginUser/')
def save_post(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    conteudo = request.POST['conteudo']
    post = Post(titulo=titulo, descricao=descricao, conteudo=conteudo)
    post.save()
    return redirect('/blog/')

#View de Post individual
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})

#View renderiza formulário de edição da postagem
@login_required(login_url='/loginForm/loginUser/')
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_edit.html', {'post':post})

#View que altera os dados da postagem
@login_required(login_url='/loginForm/loginUser/')
def update_post(request, post_id):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    conteudo = request.POST['conteudo']
    post = Post.objects.get(id=post_id)
    post.titulo = titulo
    post.descricao = descricao
    post.conteudo = conteudo
    post.save()
    return redirect(f'/blog/post/{post_id}')

#View para exclusão de postagem
@login_required(login_url='/loginForm/loginUser/')
def remove_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/blog/')