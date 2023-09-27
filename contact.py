import re
from datetime import datetime

# class that defines the contact class
class Contact:
    EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    PHONE_PATTERN = r'^\(\d{3}\) \d{3}-\d{4}$'
    def __init__(self, first_name, last_name, phone_number,
                 email, address, id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.audit = []
        self.created_on = datetime.now().strftime('%H:%M:%S')
        self.last_modified_on = datetime.now().strftime('%H:%M:%S')
    '''
    function that validates the contact requirements
    validates:
    email format, in case user decides to fill an email as it is an optional field
    phone format (###) ###-####
    mandatory fields like first name, last name and phone number
    '''
    def validate(self):
        if not re.match(self.PHONE_PATTERN, self.phone_number) or \
        self.first_name == "" or self.last_name == "" or self.phone_number == "":
            return False
        else:
            if self.email != "":
                if re.match(self.EMAIL_PATTERN, self.email):
                    return True
                else:
                    return False
            else:                                
                return True