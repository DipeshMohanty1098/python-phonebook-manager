import re
from phonebook import PhoneBook

#reusable function to search contacts
def search_contacts(phonebook):
    while True:
        print('=====================')
        print('SEARCH YOUR PHONEBOOK')
        print('=====================')
        print('Select 1 to search through contact name')
        print('Select 2 to search through contact phone number')
        print('Select 3 to return to main menu')
        try:
            option = int(input('Enter the option: '))
            if option not in range(1,4):
                print('=============')
                print('Invalid input')
                print('=============')
                continue
        except:
            print('=============')
            print('Invalid input')
            print('=============')
            continue
        if option == 1: 
            name = str(input('Enter contact name or partial name: '))
            phonebook.search_contacts_by_name(name)
            print("Search another contact?")
            print("Select 1 to search again")
            print("Select 2 to return to main menu")
            try:
                option = int(input('Enter the option: '))
                if option not in range(1,3):
                    print('=============')
                    print('Invalid input')
                    print('=============')
                    continue
            except:
                print('=============')
                print('Invalid input')
                print('=============')
                continue
            if option == 1:
                continue
            else:
                break
        if option == 2: 
            phone_number = str(input('Enter contact phone number or partial phone number: '))
            phonebook.search_contacts_by_number(phone_number)
            print("Search another contact?")
            print("Select 1 to search again")
            print("Select 2 to return to main menu")
            try:
                option = int(input('Enter the option: '))
                if option not in range(1,3):
                    print('=============')
                    print('Invalid input')
                    print('=============')
                    continue
            except:
                print('=============')
                print('Invalid input')
                print('=============')
                continue
            if option == 1:
                continue
            else:
                break
        else:
            break

#function to add a single new contact, this will be used in the "main" function:
def add_new_contact(phonebook):
    while True: 
        print('ADDING A NEW CONTACT')
        print('====================')
        print('Please enter the following details of your contact in order, fields marked with (*) are MANDATORY')
        print('First Name *')
        print('Last Name *')
        print('Phone Number *. Format - (###) ###-####')
        print('Email. Format - johndoe@email.com')
        print('Address')
        first_name = str(input('First Name: '))
        last_name = str(input('Last Name: '))
        phone_number = str(input('Phone Number: '))
        email = str(input('Email: '))
        address = str(input('Address: '))
        success = phonebook.add_contact(first_name, last_name, phone_number, email, address)
        if success: 
            print('Contact added successfully! Please find the details below. Returning to the main menu')
            phonebook.display_contacts([phonebook.contacts[-1]])
            break
        else:
            print('Failed to add contact. Please validate your details. Check if all fields adhere to the formats and required fields are not blank.')
            print('Select 1 to retry')
            print('Select 2 to return to the main menu')
            try:
                option = int(input('Enter the option: '))
                if option not in range(1,3):
                    print('========================================================')
                    print('Invalid input, please re-enter contact details correctly')
                    print('========================================================')
                    continue
            except:
                print('========================================================')
                print('Invalid input, please re-enter contact details correctly')
                print('========================================================')
                continue
            if option == 1: 
                continue
            else:
                break

# function to filter contacts based on a give timeframe, this will be used in the "main" function:
def filter_contacts_with_time(phonebook):
    while True:
        TIME_FORMAT = r'^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$'
        start_time = str(input("Enter start time in HH:MM:SS format: "))
        end_time = str(input("Enter end time in HH:MM:SS format: "))
        if not re.match(TIME_FORMAT, start_time) or not re.match(TIME_FORMAT, end_time):
            print("Invalid input, please check the start and end time formats")
            exit = str(input(("Press any key to retry or ENTER to quit to the main menu: ")))
            if exit != "":
                continue
            else:
                break
        else:
            print("=======")
            print("RESULT:")
            print("=======")
            phonebook.filter_contact_with_time(start_time, end_time)
            exit = str(input(("Press any key to filter again or ENTER to quit to the main menu: ")))
            if exit != "":
                continue
            else:
                break
        break

# function to sort contacts based on first name or last name, this will be used in the "main" function
def sort_contacts(phonebook):
    if len(phonebook.contacts) > 0:
        while True:
            print("Select 1 To sort contacts by the first name")
            print("Select 2 To sort contacts by the last name")
            try:
                option = int(input("Enter the option: "))
                if option not in range(1,3):
                    print('==========================================')
                    print('Invalid input, please enter a valid option')
                    print('==========================================')
                    exit = str(input("Press any key to retry or press ENTER to exit: "))
                    if exit != "":
                        continue
                    else:
                        break
            except:
                print('==========================================')
                print('Invalid input, please enter a valid option')
                print('==========================================')
                exit = str(input("Press any key to retry or press ENTER to exit: "))
                if exit != "":
                    continue
                else:
                    break
            if option == 1:
                temp_contacts = phonebook.contacts.copy()
                phonebook.sort_contacts_by_first_name(temp_contacts)
                exit = str(input("Press any key to sort again or press ENTER to exit: "))
                if exit != "":
                    continue
                else:
                    break
            elif option == 2:
                temp_contacts = phonebook.contacts.copy()
                phonebook.sort_contacts_by_last_name(temp_contacts)
                exit = str(input("Press any key to sort again or press ENTER to exit: "))
                if exit != "":
                    continue
                else:
                    break
    else:
        print("========================================")
        print("No contacts present in phonebook to sort")
        print("========================================")

# main function for CLI based application 
def main():
    print('Welcome to your phonebook! Please enter the corresponding number according to the action you want to perform')
    phonebook = PhoneBook()
    run = True
    while run:
        print('=========')
        print('MAIN MENU')
        print('=========')
        print('Select 1 View all your contacts')
        print('Select 2 Add a contact')
        print('Select 3 Import multiple contacts via a CSV file')
        print('Select 4 Search for contacts through name or phone number')
        print('Select 5 To update a contact')
        print('Select 7 To display phone book history')
        print('Select 8 To search for contacts created within a timeframe')
        print('Select 9 To sort contacts by the first or last name')
        print('Select 10 To view the update history of a contact')
        print('Select 11 To group contacts')
        print('Select 12 To delete a single contact')
        print('Select 13 To delete multiple contacts via a CSV file')
        print('Select 14 To exit')
        try: 
            option = int(input('Enter between choice 1 through choice 14: '))
            if option not in range(1, 15):
                print('======================================================================')
                print('Invalid input, please enter a valid option. Returning to the main menu')
                print('======================================================================')
                continue
        except:
            print('==========================================')
            print('Invalid input, please enter a valid option')
            print('==========================================')
            continue
        # flow to view all contacts in the phonebook
        if option == 1:
            if len(phonebook.contacts) > 0:
                print('FETCHED ALL {} CONTACTS: '.format(len(phonebook.contacts)))
                phonebook.display_contacts(phonebook.contacts)
            else:
                print('============================================')
                print("No contacts returned! Returning to main menu")
                print('============================================')
        # flow to add a new contact
        elif option == 2:
            add_new_contact(phonebook)
            continue
        # flow to add multiple contacts from a CSV
        elif option == 3:
            print('=============================')
            print('IMPORTING CONTACTS FROM A CSV')
            print('=============================')
            directory = str(input('Enter the filename or full directory name: '))
            phonebook.add_contacts_from_csv(directory)
        # flow to search for contacts
        elif option == 4:
            search_contacts(phonebook)
        # flow to delete a contact
        elif option == 12:
            if len(phonebook.contacts) == 0:
                print('===============================================')
                print("No contacts to delete. Returnining to main menu")
                print('===============================================')
                continue
            else:
                print("====================================")
                print("SEARCH FOR THE CONTACT TO BE DELETED")
                print("====================================")
                search_contacts(phonebook)
                continue_option = str(input('Have the ID of the desired contact? Press any button to view the history of the contact or press ENTER to return to the main menu: '))
                if continue_option == "":
                    continue
                print("======================================")
                print('SELECT ID OF THE CONTACT TO BE DELETED')
                print("======================================")
                while True:
                    try:
                        id = int(input('Enter the ID of the contact: '))
                        contact = phonebook.contacts[id-1]
                    except:
                        print('Invalid ID. Please enter a valid ID')
                        exit = str(input('Or press any key to exit or hit enter to retry: '))
                        if exit != "":
                            break
                        else:
                            continue
                    phonebook.delete_contact(id)
                    print("Contact with ID={} deleted successfuly! Returning to the main manu".format(id))
                    break
        # flow to delete contacts from a CSV
        elif option == 13:
            print('============================')
            print('DELETING CONTACTS FROM A CSV')
            print('============================')
            directory = str(input('Enter the filename or full directory name: '))
            phonebook.delete_contacts_from_csv(directory)
        # flow to display logs of the phonebook
        elif option == 7:
            phonebook.display_logs()
        # flow to filter contacts based on timestamp
        elif option == 8:
            if len(phonebook.contacts) == 0:
                print('===============================================')
                print("No contacts to filter. Returnining to main menu")
                print('===============================================')
                continue
            filter_contacts_with_time(phonebook)
        # flow to sort contacts based on first or last name
        elif option == 9:
            sort_contacts(phonebook)
        # flow to update contacts 
        elif option == 5:
            EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            PHONE_PATTERN = r'^\(\d{3}\) \d{3}-\d{4}$'
            if len(phonebook.contacts) == 0:
                print('===============================================')
                print("No contacts to update. Returnining to main menu")
                print('===============================================')
                continue
            print("====================================")
            print("SEARCH FOR THE CONTACT TO BE UPDATED")
            print("====================================")
            search_contacts(phonebook)
            continue_option = str(input('Have the ID of the desired contact? Press any button to continue to update the contact or press ENTER to return to the main menu: '))
            if continue_option == "":
                continue
            print("======================================")
            print('SELECT ID OF THE CONTACT TO BE UPDATED')
            print("======================================")
            while True:
                try:
                    id = int(input('Enter the ID of the contact: '))
                    contact = phonebook.contacts[id-1]
                except:
                    print('Invalid ID. Please enter a valid ID')
                    exit = str(input('Or press any key to exit or hit enter to retry: '))
                    if exit != "":
                        break
                    else:
                        continue
                print("You are about to edit the below contact")
                phonebook.display_contacts([phonebook.contacts[id-1]])
                print("Please enter the following information below. If you do not want to update that field, just hit ENTER to skip: ")
                first_name = str(input('Enter the first name: '))
                last_name = str(input('Enter the last name: '))
                while True:
                    phone_number = str(input('Enter the phone number in (###) ###-#### format: '))
                    if phone_number != "" and not re.match(PHONE_PATTERN, phone_number):
                        exit = str(input("Format incorrect. Press any key to retry or ENTER to skip updating the phone number: "))
                        if exit == "":
                            phone_number = ""
                            break
                        else:
                            continue
                    else:
                        break
                while True:
                    email = str(input('Enter email in johndoe@email.com format: '))
                    if email != "" and not re.match(EMAIL_PATTERN, email):
                        exit = str(input("Format incorrect. Press any key to retry or ENTER to skip updating the email"))
                        if exit == "":
                            email = ""
                            break
                        else:
                            continue
                    else:
                        break

                address = str(input('Enter address: '))
                phonebook.update_contact(id, first_name, last_name, phone_number, email, address)
                break
        # flow to view the history of a contact
        elif option == 10:
            if len(phonebook.contacts) == 0:
                print('===============================================')
                print("No contacts to view. Returnining to main menu")
                print('===============================================')
                continue
            print("======================================")
            print("SEARCH FOR THE CONTACT TO VIEW HISTORY")
            print("======================================")
            search_contacts(phonebook)
            continue_option = str(input('Have the ID of the desired contact? Press any button to view the history of the contact or press ENTER to return to the main menu: '))
            if continue_option == "":
                continue
            print("=======================================")
            print('SELECT ID OF THE CONTACT TO VIEW HISTORY')
            print("=======================================")
            while True:
                try:
                    id = int(input('Enter the ID of the contact: '))
                    contact = phonebook.contacts[id-1]
                except:
                    print('Invalid ID. Please enter a valid ID')
                    exit = str(input('Or press any key to exit or hit enter to retry: '))
                    if exit != "":
                        break
                    else:
                        continue
                phonebook.display_contact_logs(id)
                break  
        # flow to group contacts
        elif option == 11:
            if len(phonebook.contacts) == 0:
                print('===============================================')
                print("No contacts to group. Returnining to main menu")
                print('===============================================')
                continue
            while True:
                print("Select 1 to group by first name")
                print("Select 2 to group by last name")
                try:
                    choice = int(input('Enter your choice: '))
                    if choice not in range(1,3):
                        print('Invalid input. Please enter a valid input')
                        exit = str(input('Or press any key to exit or hit enter to retry: '))
                        if exit != "":
                            break
                        else:
                            continue
                except:
                    print('Invalid input. Please enter a valid input')
                    exit = str(input('Or press any key to exit or hit enter to retry: '))
                    if exit != "":
                        break
                    else:
                        continue
                phonebook.group_contacts_by_name(choice, phonebook.contacts)
                break
        # flow to quit the application       
        elif option == 14:
            run = False



if __name__ == "__main__":
    main()