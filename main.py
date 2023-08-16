from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
        # print(f'from Field: {self.value}')


class Name(Field):
    # name = True
    pass


class Phone(Field):
    # phone = None
    pass


class Record:
    def __init__(self, name: str, phones):#: list):
        self.name = Name(name).value
        self.phones = Phone(phones).value
        # self.phones = [Phone(phone).value for phone in phones]
        # print(f'from Record: {self.name.value}')
        # print(f'from Record: {self.phones.value}')
        
    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    # def find_phone(self, value):
    #     pass

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone



class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record.phones.value
        # self.data['name'] = record.name
        # self.data['phones'] = record.phones
        # return self.data['name']

    def find_record(self, value):
        return self.data.get(value)

# name = Name('Bill')
# phone = Phone('1234567890')
# rec = Record('Bill', '1234567890')
# print(rec.name)
# ab = AddressBook()
# ab.add_record(rec)
# print(ab)


# ### Checking mentor
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
    print(isinstance(ab['Bill'], Record))
    # assert isinstance(ab['Bill'], Record)
    print(isinstance(ab['Bill'].name, Name))
    # assert isinstance(ab['Bill'].name, Name)
    # print(isinstance(ab['Bill'].phones, list))
    # assert isinstance(ab['Bill'].phones, list)
    # assert isinstance(ab['Bill'].phones[0], Phone)
    # assert ab['Bill'].phones[0].value == '1234567890'
    # print('All Ok)')

