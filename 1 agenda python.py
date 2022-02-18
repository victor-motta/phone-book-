def menu():
    ReturnMainMenu = 's'
    while ReturnMainMenu == 's':
        option = input('''
        ==========================================================
                            Contact List Project
        menu:
        
        [1]REGISTER CONTACT
        [2]LIST CONTACT
        [3]DELETE CONTACT
        [4]SEARCH CONTACT BY NAME
        [5]EXIT
        ===========================================================
        SELECT ONE OPTION: 
        ''')
        if option == "1":
            registerContact()
        elif option == "2":
            listContact()
        elif option == "3":
            deleteContact()
        elif option == "4":
            searchContactByname()
        else:
            exit()
        ReturnMainMenu = input(
            "return to main menu (s/n)").lower()


def registerContact():
    idcontact = input("select your contact id: ")
    name = input("Write the contact name: ")
    telefone = input("enter the phone number of the contact: ")
    email = input("Write the email of the contact: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idcontact};{name};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Successfully recorded contact')
    except:
        print("ERROR when saving the contact")


def listContact():
    agenda = open("agenda.txt", "r")
    for contact in agenda:
        print(contact)
        agenda.close


def deleteContact():

    namedeletado = input("Enter the name to be deleted: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []

    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if namedeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'contact deleted successfully')
    listContact()


def searchContactByname():
    name = input(f'type in the name to be searched for: ').upper()
    agenda = open("agenda.txt", "r")
    for contact in agenda:
        if name in contact.split(";")[1].upper():
            print(contact)
            agenda.close


def exit():
    print(f'See you later... !')

    exit()


def main():
    menu()


main()
