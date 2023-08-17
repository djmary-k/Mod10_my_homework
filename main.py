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
    def __init__(self, name: Name, phone: Phone=None): #: phone - це не обовязковий агрумент, тому по замовчюванню None
        """в тестах ми заповнюємо класс Record обьектами класів name та phone, тому в цьому конструкторі вже приходять
        не просто строки типу 'Bill', а саме обьекти классу name
        name = Name('Bill')
        phone = Phone('1234567890')
        """
        self.name = name
        self.phone = []
        if phone:
            self.phone.append(phone)
        
    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phone:
            self.phone.append(phone_number)

    # def find_phone(self, value):
    #     pass

    def delete_phone(self, phone):
        self.phone.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phone.index(old_phone)
        self.phone[index] = new_phone



class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record # питання Чому? - тут саме треба записувати увесь обьект классу Record
        ''' я бачу цей запис в такому вигляді:
        {'Bill': ['1234567890']} тому мені здається що має бути такий запис self.data[record.name.value] = record.phone.value
        не розумію чому треба присвоювати увесь обьект классу Record, адже він повертає і"мя та список з телефоними чи ні? здається я вже запуталась..
        поясніть будь ласка
        '''
    
    def find_record(self, value):
        return self.data.get(value)



# ### Checking mentor
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)
    ##print(isinstance(ab['Bill'], Record))
    assert isinstance(ab['Bill'], Record) # оператор assert працює так, він порівнює щось, я якщо це порівняння дає false - він викликає помилку
    ##print(isinstance(ab['Bill'].name, Name))
    assert isinstance(ab['Bill'].name, Name) # тут він перевіряє що в книзі контактів під ключем 'Bill' - знаходиться обьект классу Name
    ##print(isinstance(ab['Bill'].phone, list))
    assert isinstance(ab['Bill'].phone, list)
    ##print(isinstance(ab['Bill'].phone[0], Phone))
    assert isinstance(ab['Bill'].phone[0], Phone)
    ##print(ab['Bill'].phone[0].value == '1234567890')
    assert ab['Bill'].phone[0].value == '1234567890'
    print('All Ok)')

