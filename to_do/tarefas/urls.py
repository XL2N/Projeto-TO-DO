from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_tarefas, name='tarefas'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
]