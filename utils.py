from Colorizer import Colorizer
from Phone import Phone
from Birthday import Birthday
from functools import wraps


def input_error(command=None):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as error:
                return Colorizer.error(str(error))
            except KeyboardInterrupt:
                print("Good bye!")
                exit()
            except Exception as error:
                if command == "add":
                    if len(args) < 2:
                        return Colorizer.error("Invalid input. Use 'add [name] [10 digits phone]'")
                elif command == "change":
                    if len(args) != 3 or not Phone(args[1]).value or not Phone(args[2]).value:
                        return Colorizer.error("Invalid input. Use 'change [name] [old_phone] [new_phone]'")
                elif command == "phone":
                    if len(args) != 1:
                        return Colorizer.error("Invalid input. Use 'phone [name]'")
                elif command == "add-birthday":
                    if len(args) < 2:
                        return Colorizer.error("Invalid input. Use 'add-birthday [name] [date of birth in DD.MM.YYYY format]'")
                elif command == "show-birthday":
                    if len(args) != 1:
                        return Colorizer.error("Invalid input. Use 'show-birthday [name]'")
                elif command == "change-birthday":
                    if len(args) != 2 or not Birthday(args[1]).value:
                        return Colorizer.error("Invalid input. Use 'change-birthday [name] [new_date] in DD.MM.YYYY format'")
                else:
                    return Colorizer.error("Invalid command.")
        return inner
    return decorator
