def delete_contact(contacts):
    try:
        delete_contact = input("What is the full name of the contact that you would like to delete? Please type the name exactly as it appears in your contacts: ")
        for name in contacts.copy().keys():
            if name == delete_contact:
                del contacts[name]
            else:
                raise Exception
    except Exception:
        print(f"Error: The contact you provided was not found in the Contacts, please try again.")