# ContactBook Application

The **ContactBook** application is a simple command-line program written in Python that allows users to manage their contacts. Users can add, view, delete, and update contact information, including names, phone numbers, and email addresses.

## Features

- **Add Contact**: Add a new contact with a name, phone number, and optional email address.
- **View Contacts**: View all saved contacts in a formatted list.
- **Delete Contact**: Remove a contact by their name.
- **Update Contact**: Update the phone number and/or email address of an existing contact.

## Requirements

- Python 3.7 or later

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contactbook.git
   cd contactbook
   ```

2. Run the application:
   ```bash
   python contact_book.py
   ```

## Usage

1. Launch the application using the steps above.
2. Follow the on-screen menu:

   - Enter `1` to add a new contact.
   - Enter `2` to update an existing contact.
   - Enter `3` to view all contacts.
   - Enter `4` to delete a contact.
   - Enter `5` to exit the application.

## Code Structure

### `ContactBook` Class

- **`__init__`**: Initializes an empty contact book.
- **`add_contact(name: str, phone: str, email: Optional[str] = None)`**: Adds a new contact.
- **`view_contact()`**: Displays all contacts.
- **`delete_contact(name: str)`**: Deletes a contact by name.
- **`update_contact(name: str, phone: Optional[str] = None, email: Optional[str] = None)`**: Updates contact details.

### Main Script

- Handles the user interaction loop and menu display.
- Calls the appropriate `ContactBook` methods based on user input.

## Example

### Adding a Contact
```
Enter contact name: John Doe
Enter contact phone: 123-456-7890
Enter contact email: john.doe@example.com
```

### Viewing Contacts
```
List of contacts:
Name: John Doe
Phone: 123-456-7890
Email: john.doe@example.com
--------------------------------------------------
```

### Updating a Contact
```
Enter contact name: John Doe
Enter contact phone: 987-654-3210
Enter contact email: john.new@example.com
```

### Deleting a Contact
```
Enter contact name: John Doe
Contact deleted successfully!
```
## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with suggestions or issues in the [Issues](https://github.com/your-username/contactbook/issues) section.
