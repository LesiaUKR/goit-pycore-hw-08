from Field import Field


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.value = name
