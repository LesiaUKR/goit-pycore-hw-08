from datetime import datetime
from Field import Field


class Birthday(Field):
    def __init__(self, value: str):
        try:
            if self.__is_valid(value):
                self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __is_valid(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return f'{self.value.strftime("%d.%m.%Y")}'
