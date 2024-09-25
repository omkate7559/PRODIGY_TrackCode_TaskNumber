import json
import os

# Define the file where contacts will be saved
CONTACTS_FILE = 'contacts.json'

# Load contacts from file (if the file exists)
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    
    # Add the new contact to the list
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i}: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to search for a contact by name
def search_contact(contacts):
    name = input("Enter the name to search: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return contact
    print(f"No contact found with the name {name}.")
    return None

# Function to edit a contact
def edit_contact(contacts):
    contact = search_contact(contacts)
    if contact:
        new_name = input(f"Enter new name (press Enter to keep {contact['name']}): ") or contact['name']
        new_phone = input(f"Enter new phone (press Enter to keep {contact['phone']}): ") or contact['phone']
        new_email = input(f"Enter new email (press Enter to keep {contact['email']}): ") or contact['email']
        
        contact['name'] = new_name
        contact['phone'] = new_phone
        contact['email'] = new_email
        
        save_contacts(contacts)
        print(f"Contact {new_name} updated successfully.")

# Function to delete a contact
def delete_contact(contacts):
    contact = search_contact(contacts)
    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print(f"Contact {contact['name']} deleted successfully.")

# Main program loop
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact management system
if __name__ == "__main__":
    main()
