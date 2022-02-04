def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
        ==========================================================
                            Contact List Project
        menu:
        
        [1]REGISTER CONTACT
        [2]LIST CONTACT
        [3]DELETE CONTACT
        [4]SEARCH CONTACT BY NAME
        [5]SAIR
        ===========================================================
        ESCOLHA UMA OPCÇÃO ACIMA: 
        ''')
        if opcao == "1":
            registerContact()
        elif opcao == "2":
            listContact()
        elif opcao == "3":
            deleteContact()
        elif opcao == "4":
            searchContactByname()
        else:
            sair()
        voltarMenuPrincipal = input(
            "Deseja voltar ao menu principal (s/n)").lower()


def registerContact():
    idcontact = input("escolha o id do seu contato: ")
    name = input("Escreva o nome do contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o email do contact: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idcontact};{name};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com Sucesso')
    except:
        print("ERROR na gravação do contato")


def listContact():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
        agenda.close


def deleteContact():

    nomedeletado = input("Digite o nome a ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []

    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomedeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'contato deletado com sucesso')
    listContact()


def searchContactByname():
    nome = input(f'digite o nome a ser procurado: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
            agenda.close


def sair():
    print(f'Até mais... !')

    exit()


def main():
    menu()


main()
