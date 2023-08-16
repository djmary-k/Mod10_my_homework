from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, name, phone: list):
        self.data['name'] = name
        self.data['phone'] = phone

    def get_book(self, val):
        return self.data.get(val)
    

user = AddressBook()
user.add_record('Bill', ['1234567890', '345', '987t6'])
print(user.get_book('name'), user.get_book('phone'))