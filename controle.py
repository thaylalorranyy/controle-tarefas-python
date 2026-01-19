tarefas = []

def mostrar_menu():
    print("MENU")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")

def adicionar_tarefa():
    nome = input("Digite a tarefa: ")
    tarefas.append([nome, False])
    print("Tarefa adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("Tarefas:")
    for i in range(len(tarefas)):
        status = "Concluída" if tarefas[i][1] else "Pendente"
        print(f"{1}. {tarefas[i][0]} - {status}")

def concluir_tarefa():
    listar_tarefas()
    numero = int(input("Digite o número da tarefa: ")) - 1
    tarefas[numero][1] = True
    print("Parabéns, tarefa concluída!")

def remover_tarefa():
    listar_tarefas()
    numero = int(input("Digite o número da tarefa: ")) - 1
    tarefas.pop(numero)
    print("Tarefa removida!")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
