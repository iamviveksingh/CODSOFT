
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        self.name_label = tk.Label(root, text="Name:",bg="red")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:",bg="red")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:",bg="cyan")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:",bg="cyan")
        self.address_label.pack()
        self.address_entry = tk.Entry(root, width=50)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact",bg="white", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts",bg="white", command=self.view_contacts)
        self.view_button.pack()

        self.search_label = tk.Label(root, text="Search:",fg="red")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search",fg="red", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact",bg="yellow",fg="red", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact",bg="yellow",fg="red", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contacts(self):
        contact_list = ""
        for contact in self.contacts:
            contact_list += f"Name: {contact.name}, Phone: {contact.phone}\n"
        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        query = self.search_entry.get()
        found = False
        for contact in self.contacts:
            if query in contact.name or query in contact.phone:
                messagebox.showinfo("Contact Found", f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
                break
        if not found:
            messagebox.showinfo("Not Found", "Contact not found!")

    def update_contact(self):
        name = self.name_entry.get()
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = self.phone_entry.get()
                contact.email = self.email_entry.get()
                contact.address = self.address_entry.get()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return
        messagebox.showinfo("Not Found", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return
        messagebox.showinfo("Not Found", "Contact not found!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Management System")
contact_manager = ContactManager(root)
root.mainloop()

import tkinter as tk
from tkinter import messagebox

