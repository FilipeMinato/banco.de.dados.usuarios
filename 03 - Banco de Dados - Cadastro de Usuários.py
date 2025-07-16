"""
Projeto 6 - Sistema de Cadastro de Usuários (Terminal)
------------------------------------------------------
Este sistema simples permite:
- Cadastrar usuários (nome e email)
- Listar todos os usuários cadastrados
- Editar os dados de um usuário
- Excluir um usuário da lista
- Sair do sistema

Os dados são armazenados temporariamente em uma lista de dicionários.
A navegação é feita via menu no terminal (texto).
Ideal para estudos iniciais de listas, dicionários, funções, controle de fluxo e menus interativos.
"""

# Importa a biblioteca time para criar pausas com time.sleep()
import time

# Lista global onde os usuários serão armazenados durante a execução
usuarios = []

# Função que exibe o menu principal
def mostrar_menu():
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Nome: ")       # Solicita o nome
    email = input("Email: ")     # Solicita o email
    # Adiciona o novo usuário como dicionário à lista
    usuarios.append({"nome": nome, "email": email})
    print("Usuário cadastrado com sucesso!")

# Função para listar os usuários já cadastrados
def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        # Exibe cada usuário com seu número correspondente
        for i, user in enumerate(usuarios):
            print(f"{i+1} - {user['nome']} - {user['email']}")

# Função para editar os dados de um usuário
def editar_usuario():
    listar_usuarios()  # Mostra os usuários atuais
    if len(usuarios) == 0:
        return  # Encerra se a lista estiver vazia
    try:
        # Solicita o número do usuário a ser editado
        idx = int(input("Digite o número do usuário que deseja editar: ")) - 1
        if idx < 0 or idx >= len(usuarios):
            print("Número inválido.")
            return
        # Solicita os novos dados
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        # Atualiza os dados na lista
        usuarios[idx]["nome"] = nome
        usuarios[idx]["email"] = email
        print("Usuário editado com sucesso!")
    except:
        print("Entrada inválida.")

# Função para excluir um usuário da lista
def excluir_usuario():
    listar_usuarios()  # Mostra os usuários atuais
    if len(usuarios) == 0:
        return
    try:
        # Solicita o número do usuário a ser excluído
        idx = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        if idx < 0 or idx >= len(usuarios):
            print("Número inválido.")
            return
        # Remove o usuário da lista
        usuarios.pop(idx)
        print("Usuário excluído com sucesso!")
    except:
        print("Entrada inválida.")

# Loop principal do sistema
while True:
    mostrar_menu()  # Exibe o menu principal
    escolha = input("Escolha uma opção: ")
    time.sleep(2)   # Pausa de 2 segundos para fluidez na navegação

    # Verifica qual opção foi escolhida
    if escolha == '1':
        cadastrar_usuario()
    elif escolha == '2':
        listar_usuarios()
    elif escolha == '3':
        editar_usuario()
    elif escolha == '4':
        excluir_usuario()
    elif escolha == '5':
        print("Saindo do sistema.")
        break  # Encerra o loop e finaliza o programa
    else:
        print("Opção inválida, tente novamente.")
