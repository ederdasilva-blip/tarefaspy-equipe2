'''Arquivo python'''
def listar_tarefas():
    if len(tarefas)==0:
        print("Nenhuma tarefa cadastrada")
        return
    print("\n===== TAREFAS =====")
    for indice, tarefa in enumerate(tarefas):
       if tarefa ["concluida"]:
            status = "x"
       else:
        status = " "
        print(f"{indice + 1} - [{status}]{tarefa[`descrição´]}")
                                                 