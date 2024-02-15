class Personal_Info:
    def __init__(self, name, date_of_birth, street_address, city, state, zip_code,phone_number):
        self.name = name 
        self.date_of_birth = date_of_birth 
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number 
        

name = input("What is your name?")
date_of_birth = input("What is your date of birth?")
street_address = input("What is your street address?")
city = input("What city do you live in?")
state = input("State:")
zip_code = input("Zip Code:")
phone_number = input("what is your phone number?")

class Emergency_Contact_Info: 
    def __init__(emergency_contact,emergency_contact_name, emergency_contact_phone_number, relationship):
        self.emergency_contact = emergency_contact
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone_number = emergency_contact_phone_number
        self.relationship = relationship 
    
    
emergency_contact = input("Enter Emergency Contact Info:")
emergency_contact_name = input("Name:")
emergency_contact_phone_number = input("Phone number:")
relationship  = input("What is your relationship to them?")

