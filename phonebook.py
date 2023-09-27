import csv
import time
from contact import Contact
from datetime import datetime, timezone
import re


'''
 phonebook class that houses all the contacts and change logs
 each element of the contacts list is an instance of the contact class
 "logs" is a list of operations performed on the phonebook
'''
class PhoneBook:
    def __init__(self, contacts=[], logs=[]):
        print("PhoneBook initialized")
        self.contacts = contacts
        self.logs = logs
    
    # function to display each contact in the phonebook
    def display_contacts(self,contacts):
        for contact in contacts:
            print("ID: ", contact.id, "|", "NAME: ", contact.first_name, contact.last_name, "|", 
                "PHONE NUMBER: ", contact.phone_number, "|", "EMAIL: ", contact.email , "|", 
                "ADDRESS: ", contact.address, "|", "CREATED AT: ", contact.created_on, "|", "MODIFIED AT: ", contact.last_modified_on)
            time.sleep(0.5)
    
    # function to display all the change history of a particular contact
    def display_contact_logs(self, id):
        contact_logs = self.contacts[id-1].audit
        if len(contact_logs) > 0:
            for log in contact_logs:
                print('-> ', log)
        else:
            print("===============")
            print("NO LOGS TO SHOW")
            print("===============")
    
    # function to display history of operations performed in the phonebook
    def display_logs(self):
        count = 1
        if len(self.logs) > 0:
            for log in self.logs:
                print("{}. {}".format(count, log))
                count += 1
                time.sleep(0.5)
        else:
            print("===================")
            print("No logs to show now")
            print("===================")

    #function to add a single contact to the phonebook 
    def add_contact(self, first_name, last_name, phone_number, email, address):
        contact = Contact(
            id=len(self.contacts) + 1,
            first_name=first_name,
            last_name=last_name, 
            phone_number=phone_number,
            email=email,
            address=address
        )
        # field validation to check if all the data is in the correct format
        success = contact.validate()
        if success:
            self.contacts.append(contact)
            self.logs.append("Single contact created at {}".format( datetime.now().strftime('%H:%M:%S')))
            return success
        else:
            return success
    
    #function to import multiple contacts from a CSV
    def add_contacts_from_csv(self, directory):
        valid_contact_count = 0
        invalid_contact_count = 0
        total_rows = 0
        try:
            # reads each row in the CSV file. Creates a new contact for each row
            with open(directory, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    total_rows += 1
                    contact = Contact(
                        id = len(self.contacts) + 1,
                        first_name=row['first_name'],
                        last_name = row['last_name'],
                        phone_number = row['phone_number'],
                        email = row['email'],
                        address = row['address']
                    )
                    success = contact.validate()
                    if success:
                        self.contacts.append(contact)
                        valid_contact_count += 1
                    else:
                        invalid_contact_count += 1
                        continue
            # some string formatting to delineate the number of successful and unsuccessful imports 
            if valid_contact_count == total_rows:
                print("All {} contacts added successfully!".format(total_rows))
                self.logs.append("Bulk insertion of {} contacts at {}".format(valid_contact_count,  datetime.now().strftime('%H:%M:%S')))
            if valid_contact_count > 0:
                self.display_contacts(self.contacts)
                print(valid_contact_count, "successfully imported. ", invalid_contact_count, " failed to import. Invalid email and/or phone number")
                self.logs.append("Bulk insertion of {} contacts at {}".format(valid_contact_count,  datetime.now().strftime('%H:%M:%S')))
            else: 
                print('No contacts imported, please verify the if the contacts adhere to the requirements of the email and phone number!')
        except:
            print('=============================')
            print('There was a problem in importing the contacts. Either filename does not exist or the CSV does not have the correct headers')
            print('=============================')
    
    # search the phonebook by name
    def search_contacts_by_name(self, search_query):
        search_result = []
        for contact in self.contacts:
            if ((contact.first_name + " " + contact.last_name).lower()).__contains__(search_query.lower()):
                search_result.append(contact)
        if len(search_result) > 0:
            print("=======")
            print("RESULT:")
            print("=======")
            self.display_contacts(search_result)
        else:
            print("=================================================")
            print("You do not have any contacts similar to that name")
            print("=================================================")
    
    # search the phonebook by the phone number
    def search_contacts_by_number(self, search_query):
        search_result = []
        for contact in self.contacts:
            if (contact.phone_number).__contains__(search_query):
                search_result.append(contact)
        if len(search_result) > 0:
            print("RESULT:")
            self.display_contacts(search_result)
            return search_result
        else:
            print("You do not have any contacts with a similar number")

    # function to delete a single contact through the ID of the contact
    def delete_contact(self, id):
        try:
            self.contacts.pop(id-1)
            self.logs.append("ID = {} deleted at {}".format(id, datetime.now().strftime('%H:%M:%S')))
            for i in range(len(self.contacts)):
                self.contacts[i].id = i + 1
        except:
            print('========================================')
            print("Error deleting contact, please try again")
            print('========================================')
    
    # bulk delete contacts through a CSV
    def delete_contacts_from_csv(self, directory):
        successful_deletes = 0
        unsuccessful_deletes = 0
        total_rows = 0
        try:
            with open(directory, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                cache = {}
                for row in csv_reader:
                    total_rows += 1
                    # creating a new UID to match if the contact exists in the delete batch file as well as the phonebook, this will avoid deletion of contacts with the same name
                    uid = row['first_name'][0] + row['last_name'][0] + row['phone_number'][10:]
                    cache[uid] = 0
                indices_to_be_deleted = []
                for i in range(len(self.contacts)):
                    if self.contacts[i].first_name[0] + self.contacts[i].last_name[0] + self.contacts[i].phone_number[10:] in cache:
                        indices_to_be_deleted.append(i)
                for index in indices_to_be_deleted:
                    try:
                        self.contacts.pop(index)  
                        successful_deletes += 1
                    except: 
                        continue    
            unsuccessful_deletes = total_rows - successful_deletes  
            # string formatting to delineate the number of successful and unsuccessful deletes    
            if successful_deletes == total_rows:
                print("All {} contacts deleted successfully!".format(total_rows))
                self.logs.append("Bulk delete of {} contacts at {}".format(successful_deletes,  datetime.now().strftime('%H:%M:%S')))
            if successful_deletes > 0:
                print(successful_deletes, "successfully deleted. ", unsuccessful_deletes, " failed to be deleted. There was some error in deleting the contact or the contact does not exist in the phonebook")
                self.logs.append("Bulk delete of {} contacts at {}".format(successful_deletes,  datetime.now().strftime('%H:%M:%S')))
            else: 
                print('No contacts deleted!')
            for i in range(len(self.contacts)):
                self.contacts[i].id = i + 1
        except:
            print("There was an error in deleting through the CSV. Either the file does not exist or the CSV was not formatted correctly")
    
    # function filter contacts based on their created timestamp
    def filter_contact_with_time(self,start_time, end_time):
        start_timestamp = datetime.strptime(start_time, "%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
        end_timestamp = datetime.strptime(end_time, "%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
        result = []
        for contact in self.contacts:
            created_time = datetime.strptime(contact.created_on, "%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
            if created_time >= start_timestamp and created_time <= end_timestamp:
                result.append(contact)
        if len(result) > 0:
            self.display_contacts(result)
        else:
            print("No contacts present with the given time frame")
    
    # function to sort contacts by their first name
    def sort_contacts_by_first_name(self, contacts):
        def element(contact):
            return contact.first_name
        contacts.sort(key=element)
        self.display_contacts(contacts)
    
    # function to sort contacts by their last name
    def sort_contacts_by_last_name(self, contacts):
        def element(contact):
            return contact.last_name
        contacts.sort(key=element)
        self.display_contacts(contacts)

    # function to update contacts
    def update_contact(self, id, first_name, last_name, phone_number, email, address):
        EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        PHONE_PATTERN = r'^\(\d{3}\) \d{3}-\d{4}$'
        updated_fields = []
        # giving the user the choice to update any field. if the user leaves the field blank, it will not be updated. If it is not blank it will be updated
        if first_name != "":
            updated_fields.append("First Name")
            self.contacts[id-1].first_name = first_name
        if last_name != "":
            updated_fields.append("Last Name")
            self.contacts[id-1].last_name = last_name
        if phone_number != "" and re.match(PHONE_PATTERN, phone_number):
            updated_fields.append("Phone Number")
            self.contacts[id-1].phone_number = phone_number
        if email != "" and re.match(EMAIL_PATTERN, email):
            updated_fields.append("Email")
            self.contacts[id-1].email = email
        if address != "":
            updated_fields.append("Address")
            self.contacts[id-1].address = address
        if (first_name == "" and last_name == "" and phone_number == "" and email == "" and address == ""):
            print("No updates were made. Returning to main menu")
        else:
            self.contacts[id-1].audit.append("{} changed at {}".format(','.join(updated_fields), datetime.now().strftime('%H:%M:%S')))
            self.contacts[id-1].last_modified_on = datetime.now().strftime('%H:%M:%S')
            self.logs.append("Contact ID {} changed at {}".format(id, datetime.now().strftime('%H:%M:%S')))
            print("Contact updated sucessfully!")
            self.display_contacts([self.contacts[id-1]])
    
    # function to group contacts by their first or last name
    def group_contacts_by_name(self, choice, contacts):
        # dictionary to store the indices of contacts with the same first or last name
        name_indices = {}
        if choice == 1:
            for i in range(len(contacts)):
                if contacts[i].first_name not in name_indices:
                    name_indices[contacts[i].first_name] = [i]
                else:
                    name_indices[contacts[i].first_name].append(i)

        else:
            for i in range(len(contacts)):
                if contacts[i].last_name not in name_indices:
                    name_indices[contacts[i].last_name] = [i]
                else:
                    name_indices[contacts[i].last_name].append(i)
        print("=================")
        print("GROUPING CONTACTS")
        print("=================")
        for name in name_indices:
            print("NAME ===========> {}".format(name))
            for index in name_indices[name]:
                print("ID: ", self.contacts[index].id, "|", "NAME: ", self.contacts[index].first_name, self.contacts[index].last_name, "|", 
                "PHONE NUMBER: ", self.contacts[index].phone_number, "|", "EMAIL: ", self.contacts[index].email , "|", 
                "ADDRESS: ", self.contacts[index].address, "|", "CREATED AT: ", self.contacts[index].created_on, "|", "MODIFIED AT: ", self.contacts[index].last_modified_on)
                time.sleep(0.5)



            
