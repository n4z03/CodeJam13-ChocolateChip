import re
class Chip:
    def __init__(self, first_name, last_name, phone = None, social = None, email = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.social = social
        self.email = email
    
    def addPhoneNumber(self):
        attempts = 0
        max_attempts = 10  # Set the maximum number of attempts here

        while attempts < max_attempts:
            phone = input("enter phone ")

            # Regular expression for phone number validation
            phone_pattern = re.compile(r'^\+?\d{10,15}$')
            if phone_pattern.match(phone) and len(phone) == 10:
                self.phone = phone
                return
            else:
                print("Invalid phone number, please re-enter.")
                attempts += 1

        print("Maximum attempts reached. Please try again later.")
        self.phone = phone



f = Chip("andy", "bradly")
f.addContactInfo()

print(f.phone)
# name, contact: phone number, social media, linked-in, email, type: friend, co-worker, etc etc, 