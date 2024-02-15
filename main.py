def recebe_tarefa(lista_tarefas):
	recebe_tarefa = ''
	recebe_descricao_tarefa = ''
	while len(recebe_tarefa) == 0:
		recebe_tarefa = input("Digite o título da tarefa: ")
	tarefa = {'titulo': recebe_tarefa}

	while len(recebe_descricao_tarefa) == 0:
		recebe_descricao_tarefa = input("Digite a descrição da tarefa: ")
		
	tarefa['descricao'] = recebe_descricao_tarefa
	recebe_data_conclucao_tarefa = input("Digite a data de conclusão prevista (DD/MM/AAAA): ")
	tarefa['data'] = recebe_data_conclucao_tarefa
	tarefa['status'] = "Pendente"
	lista_tarefas.append(tarefa)

	print("Tarefa adicionada com sucesso!")

def mostra_tarefas(lista_tarefas):
	if len(lista_tarefas) == 0:
		print("Lista vazia, selecione a opção de adicionar tarefas.")
		return
	print("Lista de tarefas:")

	for indice, item in enumerate(lista_tarefas):
		print(f"{indice + 1}. Título: {item['titulo']}")
		print(f"Descrição: {item['descricao']}")
		print(f"Data de conclusão: {item['data']}")
		print(f"Status: {item['status']}")
		print("-" * 20)	

def altera_status(lista_tarefas):
	escolhe_tarefa = input("Digite o número da tarefa para concluir: ")
	escolhe_tarefa_int = int(escolhe_tarefa)

	

	for indice, item in enumerate(lista_tarefas):
		if indice + 1 == escolhe_tarefa_int:
			item['status'] = "Concluída"
			print(f"{indice + 1}. Título: {item['titulo']}")
			print(f"Descrição: {item['descricao']}")
			print(f"Data de conclusão: {item['data']}")
			print(f"Status: {item['status']}")	

def apaga_tarefa(lista_tarefas):
	escolhe_tarefa = input("Digite o número da tarefa para excluir:")
	escolhe_tarefa_int = int(escolhe_tarefa)

	for indice, item in enumerate(lista_tarefas):
		if indice == escolhe_tarefa_int - 1:
			lista_tarefas.pop(indice)
		print("Tarefa excluída com sucesso.")

def main():
	print("Lista de tarefas")
	print("Selecione uma opção:")
	menu = ["1. Adicionar Tarefa", "2. Visualizar Tarefas", "3. Marcar Tarefa como Concluída", "4. Excluir Tarefa", "5. Sair"]
	for item in menu:
		print(item)

	lista_tarefas = []
	while True:
		recebe_opcao = input("Escolha uma opção de 1 à 5: ")
		match recebe_opcao:
			case "1":
				recebe_tarefa(lista_tarefas)
			case "2":
				mostra_tarefas(lista_tarefas)
			case "3":
				altera_status(lista_tarefas)
			case "4":
				apaga_tarefa(lista_tarefas)
			case "5":
				print("Programa finalizado!")
				break
			case _:
				print("Opção inválida! Tente novamente...")

if __name__ == "__main__":
	main()