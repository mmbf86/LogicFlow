# Faça uma lista de tarefas com as seguintes opções:
# - Adicionar tarefa
# - Listar tarefas
# - Remover tarefa
# - Sair

# Inicializando a lista de tarefas vazia
tarefas = []


def exibir_tarefas():
    """Exibe as tarefas."""
    if tarefas:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("\nA lista de tarefas está vazia.")


def adicionar_tarefa():
    """Adiciona uma nova tarefa."""
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada!")


def remover_tarefa():
    """Remove uma tarefa existente."""
    exibir_tarefas()
    try:
        indice = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")


def menu():
    """Exibe o menu e gerencia as interações do usuário."""
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1. Exibir tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
menu()
