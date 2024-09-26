agenda = []

def grava():
    with open('agenda.txt', 'w') as f:
        for contato in agenda:
            f.write(f"{contato['nome']},{contato['aniversario']},{contato['email']},{'|'.join(contato['telefones'])}\n")
    print("Agenda salva com sucesso.")

def le():
    global agenda
    try:
        with open('agenda.txt', 'r') as f:
            agenda = []
            for linha in f:
                nome, aniversario, email, telefones = linha.strip().split(',')
                telefones = telefones.split('|')
                agenda.append({'nome': nome, 'aniversario': aniversario, 'email': email, 'telefones': telefones})
        print("Agenda carregada com sucesso.")
    except FileNotFoundError:
        print("Arquivo da agenda não encontrado.")

def lista():
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("\nAgenda:")
        for i, contato in enumerate(agenda):
            telefones = ', '.join(contato['telefones'])
            print(f"{i}: {contato['nome']} - Aniversário: {contato['aniversario']} - Email: {contato['email']} - Telefones: {telefones}")
    print()

def apaga():
    lista()
    try:
        indice = int(input("Digite o índice do contato que deseja apagar: "))
        if 0 <= indice < len(agenda):
            del agenda[indice]
            print("Contato apagado com sucesso.")
            grava()
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

def altera():
    lista()
    try:
        indice = int(input("Digite o índice do contato que deseja alterar: "))
        if 0 <= indice < len(agenda):
            novo_nome = input("Novo nome: ")
            for contato in agenda:
                if contato['nome'].lower() == novo_nome.lower():
                    print("Erro: Já existe um contato com esse nome.")
                    return
            agenda[indice]['nome'] = novo_nome
            agenda[indice]['aniversario'] = input("Novo aniversário (DD/MM): ")
            agenda[indice]['email'] = input("Novo email: ")
            agenda[indice]['telefones'] = input("Novos telefones (separados por vírgula): ").split(", ")
            print("Contato alterado com sucesso.")
            grava()
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

def ordenar_por_nome():
    global agenda
    agenda.sort(key=lambda x: x['nome'])
    print("Agenda ordenada por nome.")

def menu():
    while True:
        print("\nMenu Principal")
        print(f"Tamanho da agenda: {len(agenda)}")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Alterar contato")
        print("4. Apagar contato")
        print("5. Ordenar por nome")
        print("6. Carregar agenda")
        print("7. Salvar agenda")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            lista()
        elif opcao == '2':
            nome = input("Nome: ")
            for contato in agenda:
                if contato['nome'].lower() == nome.lower():
                    print("Erro: Já existe um contato com esse nome.")
                    break
            else:
                aniversario = input("Aniversário (DD/MM): ")
                email = input("Email: ")
                telefones = input("Telefones (separados por vírgula): ").split(", ")
                agenda.append({'nome': nome, 'aniversario': aniversario, 'email': email, 'telefones': telefones})
                print("Contato adicionado com sucesso.")
                grava()
        elif opcao == '3':
            altera()
        elif opcao == '4':
            apaga()
        elif opcao == '5':
            ordenar_por_nome()
        elif opcao == '6':
            le()
        elif opcao == '7':
            grava()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")

menu()
