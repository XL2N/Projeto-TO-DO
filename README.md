# 📝 Projeto - TO-DO

## 📖 Sobre o Projeto

Um aplicativo completo de Lista de Tarefas (To-Do) construído com Django. O projeto inclui autenticação de usuários e um sistema CRUD (Criar, Ler, Atualizar, Excluir) completo para gerenciamento de tarefas pessoais.

## ✨ Funcionalidades

### 1. 👤 Autenticação de Usuários
* **Cadastro:** Novos usuários podem criar uma conta.
* **Login:** Usuários existentes podem acessar suas contas.
* **Logout:** Encerra a sessão do usuário.
* **Privacidade:** As tarefas são vinculadas ao usuário logado; um usuário não pode ver as tarefas de outro.

### 2. 📋 Gerenciamento de Tarefas (CRUD)
* **Criar:** Adicionar novas tarefas através de um formulário simples.
* **Listar:** Visualizar todas as tarefas do usuário, com as pendentes no topo.
* **Atualizar (Status):** Marcar/Desmarcar tarefas como concluídas diretamente na página inicial com um *checkbox*.
* **Atualizar (Texto):** Editar o título de uma tarefa existente através de um *modal* (janela pop-up), sem recarregar a página.
* **Excluir:** Remover tarefas da lista.

### 3. 🎨 Interface e UX
* **Contagem:** Exibe o número total de tarefas e o número de tarefas pendentes.
* **Design Responsivo:** Construído com **Bootstrap 5**, adaptando-se a dispositivos móveis e desktops.
* **Feedback Visual:** Tarefas concluídas são visualmente diferentes das pendentes.
* **Estilo Customizado:** Paleta de cores personalizada (Amarelo Pastel e Lilás) aplicada através de arquivos CSS estáticos.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Django
* **Frontend:** HTML5, CSS3 (com Variáveis CSS)
* **Framework CSS:** Bootstrap 5
* **Ícones:** Font Awesome
* **JavaScript:** JavaScript puro (vanilla) para alimentar o modal de edição.
* **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)

---
## 📄 Páginas Disponíveis

O projeto conta com 4 rotas principais para o usuário:

* **/ (Página Inicial):** Landing page para usuários não autenticados, com opções de Login e Cadastro.
* **/cadastro/:** Formulário de criação de conta.
* **/login/:** Formulário de autenticação.
* **/tarefas/:** Página principal da aplicação (requer login), onde o CRUD de tarefas acontece.
