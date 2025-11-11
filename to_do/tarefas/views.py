from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

@login_required
def pagina_tarefas(request):

    # TRATAR FORMULÁRIO
    if request.method == "POST":

        # EXCLUIR TAREFA
        if "excluir_tarefa" in request.POST:
            tarefa_id = request.POST.get("excluir_tarefa")
            tarefa_para_apagar = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
            tarefa_para_apagar.delete()
            return redirect("tarefas")
        
        # CONCLUIR/DESMARCAR TAREFA (LÓGICA CORRIGIDA)
        elif "concluir_tarefa" in request.POST:
            tarefa_id = request.POST.get("concluir_tarefa")
            tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
            # A mágica acontece aqui:
            # A expressão "esta_concluida" in request.POST retorna True se o checkbox estava marcado
            # e False se estava desmarcado.
            tarefa.concluida = "esta_concluida" in request.POST
            tarefa.save()
            return redirect("tarefas")

        # ADICIONAR TAREFA
        else:
            form = TarefaForm(request.POST)
            if form.is_valid():
                nova_tarefa = form.save(commit=False)
                nova_tarefa.usuario = request.user
                nova_tarefa.save()
                return redirect("tarefas")
    
    form = TarefaForm()
    lista_de_tarefas = Tarefa.objects.filter(usuario=request.user).order_by('concluida','-id')

    # CONTAGEM DE TAREFAS
    tarefas_pendentes = lista_de_tarefas.filter(concluida=False).count()
    total_tarefas = lista_de_tarefas.count()

    #Prepara os dados para enviar ao template
    context = {
        "form": form,
        "tarefas": lista_de_tarefas,
        "tarefas_pendentes": tarefas_pendentes,
        "total_tarefas": total_tarefas,
    }

    # LISTAR TAREFAS
    return render(request, "tarefas/home.html", context)

# EDITAR TAREFA
@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("tarefas")
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, "tarefas/editar.html", {"form": form, "tarefa": tarefa})

