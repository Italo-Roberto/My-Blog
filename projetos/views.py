from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Projeto
from django.contrib.auth.decorators import login_required

def index(request):
    projetos = Projeto.objects.all()
    return render(request, 'index.html', {'projetos': projetos})

#View que renderiza formulário de inserção de projetos
@login_required(login_url='/loginForm/loginUser/')
def addProjetoForm(request):
    form = ProjetoForm()
    return render(request, 'addProjetoForm.html', {'form': form})

#View que salva projetos no banco
@login_required(login_url='/loginForm/loginUser/')
def addProjeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProjetoForm()
    return render(request, 'addProjetoForm.html')

#View que renderiza formulário de edição de projeto
@login_required(login_url='/loginForm/loginUser/')
def editProjetoForm(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    return render(request, 'editProjetoForm.html', {'projeto': projeto})

#View que salva edição nos projetos
@login_required(login_url='/loginForm/loginUser/')
def editProjeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect(f'editProjetoForm/editProjeto/{projeto_id}')