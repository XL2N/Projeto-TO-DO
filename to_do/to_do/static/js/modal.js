// Aguarda o documento HTML ser completamente carregado para executar o código
document.addEventListener('DOMContentLoaded', (event) => {

    // Pega a referência para o nosso modal
    const editModal = document.getElementById('editModal');

    // Verifica se o modal realmente existe na página antes de adicionar o listener
    if (editModal) {
        // Adiciona um 'escutador' de eventos ao modal. O evento 'show.bs.modal'
        // é disparado pelo Bootstrap toda vez que o modal está prestes a ser exibido.
        editModal.addEventListener('show.bs.modal', function (event) {
            
            // Pega o botão que acionou o modal
            const button = event.relatedTarget;
            
            // Extrai as informações dos atributos data-* do botão
            const taskId = button.getAttribute('data-task-id');
            const taskTitle = button.getAttribute('data-task-title');
            
            // Pega os elementos dentro do modal que precisamos atualizar
            const modalTitle = editModal.querySelector('.modal-title');
            const modalForm = editModal.querySelector('#editForm');
            const modalInput = editModal.querySelector('#id_titulo'); // O Django geralmente cria o id como 'id_nome_do_campo'
            
            // Atualiza o título do modal
            modalTitle.textContent = 'Editando Tarefa: ' + taskTitle;
            
            // Atualiza o valor do campo de texto com o título atual da tarefa
            modalInput.value = taskTitle;
            
            // Atualiza o atributo 'action' do formulário para a URL de edição correta
            // Exemplo: /tarefas/editar/5/
            modalForm.action = `/tarefas/editar/${taskId}/`;
        });
    }
});