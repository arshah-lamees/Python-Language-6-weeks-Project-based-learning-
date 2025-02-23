import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from a file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist
    except json.JSONDecodeError:
        print("Error reading contacts file. It may be corrupted.")
        return {}

def save_contacts(contacts):
    """Saves contacts to a file."""
    try:
        with open(CONTACTS_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a contact")
    print("2. Edit a contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Exit")

def get_valid_phone():
    """Ensures the phone number is numeric."""
    while True:
        phone = input("Enter phone number: ").strip()
        if phone.isdigit():
            return phone
        else:
            print("Invalid phone number. Please enter only digits.")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists!")
        return
    phone = get_valid_phone()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def edit_contact(contacts):
    name = input("Enter contact name to edit: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    print(f"Editing contact: {name}")
    phone = input("Enter new phone number (press enter to keep current): ").strip()
    if phone:
        if not phone.isdigit():
            print("Invalid phone number format.")
            return
        contacts[name]["phone"] = phone
    email = input("Enter new email address (press enter to keep current): ").strip()
    if email:
        contacts[name]["email"] = email
    save_contacts(contacts)
    print(f"Contact {name} updated successfully!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return
    print("\nAll Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    contacts = load_contacts()  # Load contacts from file
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
