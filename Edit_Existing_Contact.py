def edit_contacts(contacts):
    import re
    try:
        edit_contact = input("What is the full name of the contact that you would like to edit? Please type the name exactly as it appears in your contacts: ")
        for name in contacts.copy().keys():
            if name == edit_contact:
                edit_info = input("What is the contact information that you would like to edit? (Phone, Email, Address, or Notes): ").lower()
                if edit_info == "phone":
                    new_phone = input("What is the new phone number for the contact? Please use the ###-###-#### format: ")
                    if re.search(r"\d{3}-\d{3}-\d{4}", new_phone):
                        contacts[name]["Phone"] = new_phone
                    else:
                        raise Exception
                elif edit_info == "email":
                    new_email = input("What is the contact's new email address? Please use the emailaddress@domain.com format: ")
                    if re.search(r"[A-Za-z0-9._%+-]+@[A-Z|a-z]{2,}", new_email):
                        contacts[name]["Email"] = new_email
                    else:
                        raise Exception
                elif edit_info == "address":
                    new_address = input("What is the contact's mailing address? Please use the #### Street Name, City, State, Zip Code format: ")
                    if re.search(r"\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?, (?:[A-Z][a-z.-]+[ ]?)+, AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY, \b\d{5}(?:-\d{4})?\b", new_address):
                        contacts[name]["Address"] = new_address
                    else:
                        raise Exception
                elif edit_info == "notes":
                    update_notes = input("Please enter any notes you wish to save in regards to this contact, if you have no notes for this contact please enter 'none': ")
                    if re.search(r"^\s*$", update_notes):
                        raise Exception
                    else:
                        contacts[name]["Notes"] = update_notes
            else:
                raise Exception
    except Exception:
        print(f"Error: I'm sorry, but the information you provided is not in the acceptable format. Please try again.")