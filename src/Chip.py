import re
class Chip:
    def __init__(self, first_name, last_name, phone = None, social = None, email = None):
        self.attribute_list = []
        self.information_list = []

        self.attribute_list.append("First Name")
        self.information_list.append(first_name)

        self.attribute_list.append("Last Name")
        self.information_list.append(last_name)

        self.attribute_list.append("Phone")
        self.information_list.append(phone)

        self.attribute_list.append("Social")
        self.information_list.append(social)
        
        self.attribute_list.append("Email")
        self.information_list.append(email)

    def add_attribute(self, attribute):
        self.attribute_list.append(attribute)
        self.information_list.append("")
   
    def change_attribute(self, index, attribute):
        self.attribute_list[index] = attribute
   
    def change_information(self, index, information):
        self.information_list[index] = information

    def delete_attribute(self, index):
        self.attribute_list.remove(index)
        self.information_list.remove(index)

    def swap(self, index1, index2):
        self.attribute_list[index1], self.attribute_list[index2] = self.attribute_list[index2], self.attribute_list[index1]
        self.information_list[index1], self.information_list[index2] = self.information_list[index2], self.information_list[index1]
        
    def addPhoneNumber(self):
        """ authentication should happen at frontend
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
        """
        
f = Chip("andy", "bradly")
f.addContactInfo()

print(f.phone)
# name, contact: phone number, social media, linked-in, email, type: friend, co-worker, etc etc, 