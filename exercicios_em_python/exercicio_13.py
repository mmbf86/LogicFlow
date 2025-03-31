# Faça um sistema de pedidos de comida
# com as seguintes opções:
# - Adicionar item ao pedido
# - Listar itens do pedido
# - Remover item do pedido
# - Finalizar pedido
# - Sair

import datetime

todos_pedidos = []


def adicionar_item(pedidos):
    item = input("Digite o nome do item que deseja adicionar ao pedido: ")
    if item:
        pedidos.append(item)
        print(f"Item '{item}' adicionado ao pedido!")
    else:
        print("Nome do item não pode ser vazio.")
    return pedidos


def listar_itens(pedidos):
    if pedidos:
        print("\nItens no pedido:")
        for i, item in enumerate(pedidos, 1):
            print(f"{i}. {item}")
    else:
        print("\nO pedido está vazio.")
    return pedidos


def remover_item(pedidos):
    listar_itens(pedidos)
    if pedidos:
        try:
            indice = int(
                input("\nDigite o número do item que deseja remover: "))
            if 1 <= indice <= len(pedidos):
                item_removido = pedidos.pop(indice - 1)
                print(f"Item '{item_removido}' removido do pedido!")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    return pedidos


def finalizar_pedido(pedidos):
    print("\nFinalizando o pedido...")
    listar_itens(pedidos)
    total_itens = len(pedidos)
    print(f"Total de itens no pedido: {total_itens}")

    if pedidos:
        data_hora_pedido = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        todos_pedidos.append(
            {"pedido": pedidos[:], "data e hora": data_hora_pedido})

    print("Obrigado por usar o sistema de pedidos!")
    return True

# Incremento do Código
def salvar_extrato():
    if todos_pedidos:
        nome_arquivo = f"Extrato pedidos {datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write("Extrato de Pedidos do Dia:\n")
            for i, registro in enumerate(todos_pedidos, 1):
                arquivo.write(
                    f"Pedido {i} (Data e Hora: {registro['data e hora']}):\n")
                arquivo.write("\n".join(registro["pedido"]) + "\n\n")
        print(f"Extrato salvo com sucesso no arquivo: {nome_arquivo}")
    else:
        print("Nenhum pedido foi realizado ainda. Nada para salvar.")
#Incremento do Código

def menu():
    # Inicializando a lista de pedidos vazia
    pedidos = []
    while True:
        print("\n--- MENU DE PEDIDOS ---")
        print("1. Adicionar item ao pedido")
        print("2. Listar itens do pedido")
        print("3. Remover item do pedido")
        print("4. Finalizar pedido")
        print("5. Salvar extrato dos pedidos do dia")
        print("6. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                pedidos = adicionar_item(pedidos)
            elif opcao == 2:
                pedidos = listar_itens(pedidos)
            elif opcao == 3:
                pedidos = remover_item(pedidos)
            elif opcao == 4:
                if finalizar_pedido(pedidos):
                    break
            elif opcao == 5:
                salvar_extrato()
            elif opcao == 6:
                print("Saindo do programa. Até mais!")
                return
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    while True:
        novo_pedido = input(
            "\nDeseja fazer um novo pedido? (sim/não): ").strip().lower()
        if novo_pedido == 'sim':
            print("Iniciando um novo pedido...")
            menu()
            break
        elif novo_pedido == 'não':
            print("Encerrando o sistema. Até mais!")
            return  # Encerra todo o programa
        else:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")


menu()
