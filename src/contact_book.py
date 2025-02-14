from typing import Optional


class ContactBook:
    """
    A class to manage a contact book with functionalities to add, view, delete, and update contacts.
    """

    def __init__(self) -> None:
        self.contacts = {}
        """
        Initialize an empty contact book.
        """

    def add_contact(self, name: str, phone: str, email: Optional[str] = None) -> None:
        """
        Add a new contact to the contact book.

        :param name: The name of the contact.
        :param phone: The phone number of the contact.
        :param email: The email address of the contact (optional).
        """
        if name in self.contacts:
            print("Contact already exists")
            return
        
        self.contacts[name] = {}
        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email

    def view_contact(self) -> None:
        """
        Display all contacts in the contact book.
        """
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("_" *50)

    def delete_contact(self, name: str) -> None:
        """
        Delete a contact by name from the contact book.

        :param name: The name of the contact to delete.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("contact deleted successfully!")
        else:
            print("contact not found!")

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> None:
        """
        Update an existing contact's phone number and/or email address.

        :param name: The name of the contact to update.
        :param phone: The new phone number (optional).
        :param email: The new email address (optional).
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print("contact updated successfully!")
            return
        print("contact not found!")


if __name__ == "__main__":
    new_book = ContactBook()
    while True:
        print("\n\nWelcome to Contactbook application!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Quit")

        user_choice = input("Please choose an option: ")
        if user_choice == "5":
            break

        elif user_choice == "1":
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            new_book.add_contact(name, phone, email)
        
        elif user_choice == "2":
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            new_book.update_contact(name, phone, email)
        
        elif user_choice == "3":
            print("\n\nList of contacts: ")
            new_book.view_contact()
        
        elif user_choice == "4":
            name = input("Enter contact name: ")
            new_book.delete_contact(name)