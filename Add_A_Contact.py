def add_contact(contacts):
    import re
    try:
        first_name = input("What is the first name of the contact you wish to add?: ").capitalize()
        if re.search(r"A-Za-z+-", first_name) == False:
            raise Exception
        else:
            last_name = input("What is the last name of the contact you wish to add?: ").capitalize()
            if re.search(r"A-Za-z+-", last_name) == False:
                raise Exception
            else:
                phone = input("What is the contact's phone number? Please use the ###-###-#### format: ")
                if re.search(r"\d{3}-\d{3}-\d{4}", phone) == False:
                    raise Exception
                else:
                    email = input("What is the contact's email address? Please use the emailaddress@domain.com format: ")
                    if re.search(r"[A-Za-z0-9._%+-]+@[A-Z|a-z]{2,}", email) == False:
                        raise Exception
                    else:
                        address = input("What is the contact's mailing address? Please use the #### Street Name, City, State Zip Code format: ")
                        if re.search(r"\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?, (?:[A-Z][a-z.-]+[ ]?)+, AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY, \b\d{5}(?:-\d{4})?\b", address) == False:
                            print("I'm sorry, I didn't understand. Please try again.")
                        else:
                            notes = input("Please enter any notes you wish to save in regards to this contact, if you have no notes for this contact please enter 'none': ")
                            if re.search(r"", notes) == True:
                                raise Exception
                            else:
                                contacts[f"{first_name} {last_name}"] = {"Phone": phone, "Email": email, "Address": address, "Notes": notes}
    except Exception:
        print(f"Error: I'm sorry, but the information you provided is not in the acceptable format. Please try again.")