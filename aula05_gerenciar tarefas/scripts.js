document.addEventListener('DOMContentLoaded', function () {
    const userNameInput = document.getElementById('userName');
    const addUserBtn = document.getElementById('addUserBtn');
    const userList = document.getElementById('userList');
    const taskUserSelect = document.getElementById('taskUser');
    const taskNameInput = document.getElementById('taskName');
    const taskStatusSelect = document.getElementById('taskStatus');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    let users = JSON.parse(localStorage.getItem('users')) || [];
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    //Atualiza lista de usuários no UI
    function updateUserListUI() {
        userList.innerHTML = '';
        taskUserSelect.innerHTML = '<option selected>Escolha um usuário</option>';
        
        users.forEach((user, index) => {
            const userListItem = document.createElement('li');
            userListItem.className = 'list-group-item user-list-item';
            userListItem.innerHTML = `
                ${user}
                <button class="btn btn-danger btn-sm" onclick="deleteUser(${index})">Remover</button>
            `;
            userList.appendChild(userListItem);

            const option = document.createElement('option');
            option.value = user;
            option.textContent = user;
            taskUserSelect.appendChild(option);
        });
    }

    // Exibir as tarefas
    function displayTasks() {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const taskItem = document.createElement('div');
            taskItem.className = 'task-item';
            taskItem.innerHTML = `
                <span><strong>${task.user}</strong>: ${task.name}</span>
                <div class="task-actions">
                    <span class="task-status badge bg-secondary">${task.status}</span>
                    <button class="btn btn-success btn-sm" onclick="editTask(${index})">Editar</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteTask(${index})">Remover</button>
                </div>
            `;
            taskList.appendChild(taskItem);
        });
    }

    // Função para adicionar usuário
    function addUser() {
        const userName = userNameInput.value.trim();

        if (userName && !users.includes(userName)) {
            users.push(userName);
            localStorage.setItem('users', JSON.stringify(users));
            userNameInput.value = '';
            updateUserListUI();
        } else {
            alert('Por favor, insira um nome de usuário único.');
        }
    }

    // Função para remover um usuário
    window.deleteUser = function(index) {
        const removedUser = users.splice(index, 1)[0];
        tasks = tasks.filter(task => task.user !== removedUser);
        localStorage.setItem('users', JSON.stringify(users));
        localStorage.setItem('tasks', JSON.stringify(tasks));
        updateUserListUI();
        displayTasks();
    }

    // Adicionar nova tarefa
    function addTask() {
        const user = taskUserSelect.value;
        const name = taskNameInput.value;
        const status = taskStatusSelect.value;

        if (user !== 'Escolha um usuário' && name.trim() !== '') {
            tasks.push({ user, name, status });
            localStorage.setItem('tasks', JSON.stringify(tasks));
            taskNameInput.value = '';
            taskUserSelect.selectedIndex = 0;
            taskStatusSelect.selectedIndex = 0;
            displayTasks();
        } else {
            alert('Por favor, selecione um usuário e digite uma tarefa.');
        }
    }

    // Editar tarefa
    window.editTask = function(index) {
        const task = tasks[index];
        taskNameInput.value = task.name;
        taskUserSelect.value = task.user;
        taskStatusSelect.value = task.status;

        addTaskBtn.textContent = 'Salvar Alterações';
        addTaskBtn.onclick = function() {
            tasks[index] = {
                user: taskUserSelect.value,
                name: taskNameInput.value,
                status: taskStatusSelect.value
            };
            localStorage.setItem('tasks', JSON.stringify(tasks));
            addTaskBtn.textContent = 'Adicionar Tarefa';
            addTaskBtn.onclick = addTask;
            taskNameInput.value = '';
            taskUserSelect.selectedIndex = 0;
            taskStatusSelect.selectedIndex = 0;
            displayTasks();
        };
    }

    // Função para remover uma tarefa
    window.deleteTask = function(index) {
        tasks.splice(index, 1);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        displayTasks();
    }

    // Eventos de clique para adicionar usuário e tarefa
    addUserBtn.addEventListener('click', addUser);
    

    // Carregar dados e exibir ao carregar a página
    updateUserListUI();
    displayTasks();
});
