contacts = {
    1 : {
        "name" : "Aryan",
        "number" : 12345,
    },
    2 : {
        "name" : "Temp",
        "number" : 567891,
    },
}

def showMenu():
    print("Welcome to Aryan's Contact List. What do you want to do?")
    print("1. View contact")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Exit")

    selectMenu()

def selectMenu():
    repeat = True
    while repeat == True:
        try:
            option = int(input("Choose[1-4]: "))
        except ValueError:
            print("Please input number.")
            option = 0
        if option > 0 and option < 6: repeat = False
        if option == 1:
            showContacts()
            showMenu()
        elif option == 2:
            print("\n===========")
            print("Add Contact")
            print("===========")
            addContact()
            showMenu()
        elif option == 3:
            deleteContact()
            showMenu()
        elif option == 4:
            break
        else: 
            print("Option unavailable.")

def showContacts():
    num = 1
    print("==========================================")
    print("|No.| Name            | Number           |")
    print("==========================================")
    for contact in contacts.values():
        print("|{no} .| {name:<15} | {number:<15}  "
        .format(no = num, name = contact["name"], 
                number = contact["number"]))
        num += 1
    print("==========================================")

def addContact():
    contact_order = list(contacts.keys())[-1] + 1
    while True:
        try:
            name = str(input("Enter contact name: "))
            number = int(input("Enter contact number: "))
            # add data to contacts
            contacts[contact_order] = {
                "name" : "{}". format(name),
                "number" : number,
            }
            print("Data " + name + " added succesfully!\n")
            break
        except ValueError:
            print("Wrong input. Please enter a correct format.\n")
            break

def deleteContact():
    isDelete = False
    showContacts()
    name = str(input("Enter contact's name you want to delete: "))
    for contact_id, contact_info in list(contacts.items()):
        if contact_info["name"] == name:
            del contacts[contact_id]
            showContacts()
            print("Data '{}' deleted Succesfully!\n".format(name))
            isDelete = True
    if isDelete == False: print("Data not found!\n")

showMenu()