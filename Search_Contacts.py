def search_contacts(contacts):
    try:
        search_contact = input("What is the full name of the contact that you would like to edit? Please type the name exactly as it appears in your contacts: ")
        found = False
        for name, details in contacts.items():
            if name == search_contact:
                found = True
        if found == True:
            print(f"{name}: {details}")
        else:
            raise Exception
    except Exception:
        print("Error: The contact you are looking for was not found, please try again.")