from Name import Name
from Phone import Phone
from Birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {
            '; '.join(p.value for p in self.phones)}"
        if self.birthday:
            result += f", birthday: {self.birthday}"
        return result

    def add_phone(self, phone):
        if phone in self.phones:
            raise ValueError("Phone number already exists")
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        raise ValueError("Phone number not found")

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def update_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)
