print("====================")
print("     Tarefaspy")
print("====================")

print("1 - Adicionar tarefa")
print("2 - Listar tarefas")
print("3 - Concluir tarefa")
print("4 - Remover tarefa")
print("0 - Sair")

exibir_menu()

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
    print("\nEncerrando o TaskPy...")