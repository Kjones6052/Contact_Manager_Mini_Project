# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).

def import_contacts(contacts):
    with open('Contacts.txt', 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                contacts[key] = eval(value)