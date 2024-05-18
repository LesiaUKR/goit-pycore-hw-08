# Theme 12. Homework. Serialization and Object Copying in Python goit-pycore-hw-08

### Serialization and deserialization of data using pickle

### Working with files

## Technical task description

> [!TIP]☝ In this homework assignment, you need to add functionality to save the address book to disk and restore it from disk.

For this purpose, you should choose the pickle protocol for data serialization/deserialization and implement methods that allow you to save all data to a file and load them from a file.

**The main goal** is to ensure that the application does not lose data after exiting and restores them from the file when launched. The address book with which we worked in the previous session should be preserved.

Implement functionality to save the state of the **AddressBook** to a file when closing the program and restore the state when launching it.

Example code that may be useful:

Serialization with pickle

```
import pickle

def save_data(book, filename="addressbook.pkl"):
with open(filename, "wb") as f:
pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
try:
with open(filename, "rb") as f:
return pickle.load(f)
except FileNotFoundError:
return AddressBook() # Return a new address book if the file is not found
```

Integration of saving and loading into the main loop

```
def main():
book = load_data()

    # Main program loop

    save_data(book)  # Call before exiting the program
```

> [!NOTE] These examples will help you in implementing the homework assignment.

### Evaluation Criteria:

1. Implemented protocol for data serialization/deserialization using pickle
2. All data should be saved when exiting the program
3. The AddressBook in the new session should be the same as it was in the previous run.
