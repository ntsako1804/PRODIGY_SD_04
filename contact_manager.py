import json
import os

#File used to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
  if os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "r") as file:
      return json.load(file) 
  return {}


# Save contacts to file
def save_contacts(contacts):
  with open(CONTACTS_FILE, "w") as file:
    json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email address: ")


  contacts[name] = {"phone": phone, "email": email}
  save_contacts(contacts)
  print(f"Contact '{name}' added succesfully")


# View all contacts
def view_contacts(contacts):
  if not contacts:
    print("No contacts found.")
  else:
    print("\nContact List:")
    for name, info in contacts.items():
      print(f"Name: {name}")
      print(f"Phone: {info['phone']}")
      print(f"Email: {info['email']}")
      print("-"*20)


# Edit an existing contact
def edit_contact(contacts):
  name = input("Enter the name of the contact to edit: ")

  if name in contacts:
    phone = input("Enter new phone number (or press Enter to keep current): ")
    email = input("Enter new email address (or press Enter to keep current): ")

    if phone:
      contacts[name]["phone"] = phone
    if email:
      contacts[name]["email"] = email

    save_contacts(contacts)
    print(f"Contact '{name}' updated succesfully")
  else:
    print(f"Contact '{name}' not found")


# Delete a contact
def delete_contact(contacts):
  name = input("Enter the name of the contact to delete: ")


  if name in contacts:
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted succesfully")
  else:
    print(f"Contact '{name}' not found")


# Main menu
def main():
  contacts = load_contacts()

  while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
      add_contact(contacts)
    elif choice == "2":
      view_contacts(contacts)
    elif choice == "3":
      edit_contact(contacts)
    elif choice == "4":
      delete_contact(contacts)
    elif choice == "5":
      print("Existing the program. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again")


# Run the program
if __name__ == "__main__":
  main()

