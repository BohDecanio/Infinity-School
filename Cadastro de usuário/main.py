
usuarios = []

def gerar_id():
    if usuarios:
        return usuarios[-1]['id'] + 1
    else:
        return 1
    
def adicionar_usuario(nome, usuario, senha, email):
    if not nome or not usuario:
        print("Erro: Nome e Usuário não podem ser nulos.")
        return

    for user in usuarios:
        if user['usuario'] == usuario:
            print("Erro: Usuário já existente. Escolha outro.")
            return

        if user['email'] == email:
            print("Erro: E-mail já existente. Escolha outro.")
            return

    if len(senha) < 6:
        print("Erro: A senha deve ter pelo menos 6 caracteres.")
        return

    novo_usuario = {
        'id': gerar_id(),
        'nome': nome,
        'usuario': usuario,
        'senha': senha,
        'cargo': 'Membro',
        'email': email,
        'verificar': False
    }

    for verificar_id in usuarios:
        if verificar_id['id'] == 1:
            verificar_id['cargo'] = 'Admin'
            verificar_id['verificar'] = True

    usuarios.append(novo_usuario)
    print("Usuário adicionado com sucesso!")

adicionar_usuario('italo', 'italoUser', '123456', 'italo@mail.com')


for user in usuarios:
    print(f"ID: {user['id']}, Nome: {user['nome']}, Usuário: {user['usuario']}, Cargo: {user['cargo']}, {'Verificado' if user['verificar'] else 'Não verificado'}")


__________

'''adicionar usuários,senha tem que ser de minimo 6 - usuario nao pode em branco e nao pode repetir, 
tem que dar erro se repetir.emails nao pode repetir. id deve ser dinamico

mostrar todos os usuários, 
mostrar um usuário específico pelo nome de usuário, 
realizar login, 

deletar um usuário (caso esteja logado e seja um admin).'''