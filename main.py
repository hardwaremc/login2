estudantes = []
id = 1

def adicionar_estudante():
  global id
  nome = input("Digite o nome do estudante: ")
  idade = input("Digite a idade do estudante: ")
  curso = input("Digite o curso do estudante")
  estudante = {
    "id" : id,
    "nome" : nome,
    "idade" : idade,
    "curso" : curso
  }
  estudantes.append(estudante)
  print(f"Estudante {nome} adicionado com sucesso com ID {id}")
  id +=1

def remover_estudante():
  criterio = input("Deseja remover por (1) Nome ou (2) ID?")
  if criterio == "1":
    nome = input("Digite o nome do estudante a ser removido: ")
    for estudante in estudantes:
      if estudante["id"] == id:
        estudantes.remove(estudante)
        print(f"Estudante com ID {id} removido com sucesso!")
        return
    print(f"Estudante {nome} não encontrado.")
  elif criterio == "2":
    id = int(input("Digite o ID do estudante a ser removido: "))
    for estudante in estudantes:
      if estudante["id"] == id:
        estudantes.remove(estudante)
        print(f"Estudante com ID {id} removido com sucesso!")
        return
      print(f"Estudante com ID {id} não encontrado")
    else:
      print("Opção inválida")

def buscar_estudante():
  criterio = input("Deseja buscar por (1) Nome ou (2) ID? ")
  if criterio == "1":
    nome = input("Digite o nome do estudante a ser buscado: ")
    for estudante in estudantes:
      if estudante["nome"] == nome:
        print(f"Estudante encontrado: ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")
        return
      print(f"Estudante com ID {id} não encontrado.")
    else:
      print("Opção inválida.")

def listar_estudantes():
  if not estudantes:
    print("Nenhum estudante cadastrado. ")
    return
  for estudante in estudantes:
    print(f"ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")

def menu():
  while True:
    print("\nMenu:")
    print("1. ADICIONAR ESTUDANTE")
    print("2. REMOVER ESTUDANTE")
    print("3. BUSCAR ESTUDANTE")
    print("4. LISTAR ESTUDANTE")
    print("5. SAIR")
    opcao = input("Escolha uma opção: ")

    if opcao =="1":
      adicionar_estudante()
    elif opcao =="2":
      remover_estudante()
    elif opcao == "3":
      buscar_estudante()
    elif opcao == "4":
      listar_estudantes()
    elif opcao == "5":
      print("Saindo do programa. ")
      break
    else:
      print("Opção inválida, por favor escolha uma opção válida ")

menu()
      
  
