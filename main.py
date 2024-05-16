from Addressbook import AddressBook
from Record import Record
from Colorizer import Colorizer
from utils import input_error
from Phone import Phone
from Birthday import Birthday

contact_not_found_message = Colorizer.error("Contact not found.")


@input_error("add")
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return Colorizer.error("Invalid input. Use 'add [name] [10 digits phone]'")
    name, phone = args[:2]
    record = book.find(name)
    message = Colorizer.success("Contact updated.")
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = Colorizer.success("Contact added.")
    else:
        if phone in [p.value for p in record.phones]:
            return Colorizer.error("Phone number already exists for this contact.")
    if phone:
        record.add_phone(phone)
    return message


@input_error("change")
def change_contact(args, book: AddressBook):
    if len(args) != 3 or not Phone(args[1]).value or not Phone(args[2]).value:
        return Colorizer.error("Invalid input. Use 'change [name] [old_phone] [new_phone]'")
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return contact_not_found_message
    else:
        record.edit_phone(old_number, new_number)
        return Colorizer.success("Phone changed")


@input_error("phone")
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        return contact_not_found_message
    return record


@input_error("add-birthday")
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return Colorizer.error("Invalid input. Use 'add-birthday [name] [date of birth in DD.MM.YYYY format]'")
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return Colorizer.success("Birthday added.")
    else:
        return contact_not_found_message


@input_error("show-birthday")
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return Colorizer.warn('Birthday not added to this contact.')
    else:
        return contact_not_found_message


@input_error("change-birthday")
def change_birthday(args, book: AddressBook):
    name, new_birthday = args
    record = book.find(name)
    if record is None:
        return contact_not_found_message
    else:
        record.birthday = Birthday(new_birthday)
        return Colorizer.success("Birthday changed")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print(Colorizer.info("Welcome to the assistant bot!"))
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        match command:
            case "hello":
                print("How can I help you?")
            case "close" | "exit":
                print("Good bye!")
                break
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "change-birthday":
                print(change_birthday(args, book))
            case "birthdays":
                print(book.get_upcoming_birthdays())
            case _:
                print(Colorizer.error("Invalid command."))


if __name__ == "__main__":
    main()
