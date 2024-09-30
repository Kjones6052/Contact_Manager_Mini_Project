# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).
from Add_A_Contact import add_contact
from Delete_Contact import delete_contact
from Display_Contacts import display_contacts
from Display_Menu import display_menu
from Edit_Existing_Contact import edit_contacts
from Export_Contacts import export_contacts
from Import_Contacts import import_contacts
from Search_Contacts import search_contacts

contacts = {}
intro = "Welcome to the Contact Management System!"

print(intro)
display_menu()

while True:
    user_continue = input("Would you like to continue? (yes/no): ").lower()
    if user_continue == "yes":
        user_action = input("What would you like to do? You can also type 'Menu' for a list of options: ").lower()
        if user_action == "menu":
            display_menu()
        elif user_action == "add":
            add_contact(contacts)
        elif user_action == "delete":
            delete_contact(contacts)
        elif user_action == "edit":
            edit_contacts(contacts)
        elif user_action == "search":
            search_contacts(contacts)
        elif user_action == "display":
            display_contacts(contacts)
        elif user_action == "export":
            export_contacts(contacts)
        elif user_action == "import":
            import_contacts(contacts)
        elif user_action == "quit":
            break
        else:
            print("I'm sorry, I did not understand your selection. Please try again.")
    elif user_continue == "no":
        break
    else:
        print("I'm sorry, I did not understand your selection. Please try again.")