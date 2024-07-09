contacts = []

def add_contact():
    name= input("Enter name: ")
    phone= input("Enter phone number: ")
    email= input("Enter email : ")
    address= input("Enter address: ")
    contact ={
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)

def view_contact():
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['name']} - {contact['phone']} -{contact['email']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    result = [contact for contact in contact if query in contact['name'] or query in contact['phone']]
    for contact in result:
        print(f"{contact['name']} - {contact['phone']}")

def update_contact():
    view_contact()
    contact_index = int(input("Enter the number of the contact to udate: ")) -1
    if 0<= contact_index < len(contacts):
        contacts[contact_index]['name'] = input("Enter the new name")
        contacts[contact_index]['phone'] = input("Enter the new phone number")
        contacts[contact_index]['email'] = input("Enter the new email")
        contacts[contact_index]['address'] = input("Enter the new address")
        print("Contact updated successfully!")
    else:
        print("invalid contact number.")

def delete_contact():
    view_contact()
    contact_index = int(input("Enter the number to delete: ")) -1
    if 0 <= contact_index < len(contacts):
        contacts.pop(contact_index)
        print("Contact deleted successfully!")
    else:
        print("invalid contact number.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        chioce = input("choose an option: ")
        if chioce =='1':
            add_contact()
        elif chioce == '2':
            view_contact()
        elif chioce == '3':
            search_contact()
        elif chioce == '4':
            update_contact()
        elif chioce == '5':
            delete_contact()
        elif chioce == '6':
            break
        else:
            print("Invalid choic. Please try again.")

if __name__== "__main__":
    main()