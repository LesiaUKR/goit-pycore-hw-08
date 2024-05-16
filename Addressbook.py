from collections import UserDict
from Record import Record
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def __str__(self):
        lines = []

        for _, record in self.data.items():
            lines.append(f'{record}')

        return "\n".join(lines)

    def add_record(self, record: Record):
        if record.name.value in self.data:
            print(f"Contact with name {record.name.value} already exists")
        else:
            self.update({record.name.value: record})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact with name {name} not found")

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []

        today = datetime.today().date()

        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)

                next_week = today + timedelta(days=7)
                if today <= birthday_this_year <= next_week:
                    upcoming_birthdays.append(
                        {"name": name, "birthday_date": birthday_this_year.strftime("%d.%m.%Y")})

        return upcoming_birthdays
