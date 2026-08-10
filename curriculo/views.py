from django.shortcuts import render,get_object_or_404,redirect
from .models import Projeto
from .forms import ProjetoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    contexto={"projetos":Projeto.objects.all()}
    return render(request,'curriculo/home.html',contexto)


def detalhe(request,id):
    projeto=get_object_or_404(Projeto,id=id)
    contexto={"projeto":projeto}
    return render(request,'curriculo/detalhe.html',contexto)

@login_required
def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProjetoForm()

    contexto = {"form": form}
    return render(request, "curriculo/form.html", contexto)

@login_required
def editar_projeto(request,id):
    projeto=get_object_or_404(Projeto,id=id)
    if request.method == "POST":
        form=ProjetoForm(request.POST,instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form=ProjetoForm(instance=projeto)


    contexto={"form":form}
    return render(request,"curriculo/form.html",contexto)


@login_required
def excluir_projeto(request,id):
    projeto=get_object_or_404(Projeto,id=id)
    if request.method == "POST":
        projeto.delete()
        return redirect("home")

    contexto={"projeto":projeto}
    return render(request,'curriculo/excluir.html',contexto)




