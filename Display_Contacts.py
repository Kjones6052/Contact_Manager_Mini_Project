def display_contacts(contacts):
    for contact, details in contacts.items():
        print(f"{contact}: ")
        for key, value in details.items():
            print(f"{key}: {value}")