def export_contacts(contacts):
    with open('Contacts.txt', 'w') as file:
        for name, details in contacts.items():
            file.write(f"{name}: {details}\n")