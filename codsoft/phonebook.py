import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("H4CK3R C0NT4CT M4N4G3R")
        self.master.configure(bg="#0d0208")
        
        self.contacts = {}
        
        self.name_label = tk.Label(master, text="Name:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(master, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(master, text="Phone:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(master, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(master, text="Email:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(master, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(master, text="Address:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.address_entry = tk.Entry(master, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.add_button.grid(row=4, columnspan=2, padx=10, pady=10)
        
        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.search_button.grid(row=5, columnspan=2, padx=10, pady=5)
        
        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.update_button.grid(row=6, columnspan=2, padx=10, pady=5)
        
        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.delete_button.grid(row=7, columnspan=2, padx=10, pady=5)
        
        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.view_button.grid(row=8, columnspan=2, padx=10, pady=5)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required fields!")
        
    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact_info = self.contacts[name]
            messagebox.showinfo("Contact Info", f"Name: {name}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\nAddress: {contact_info['Address']}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contact found with the name: {name}")
        
    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            self.contacts[name]["Phone"] = phone
            self.contacts[name]["Email"] = email
            self.contacts[name]["Address"] = address
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Contact Not Found", f"No contact found with the name: {name}")
            
    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Contact Not Found", f"No contact found with the name: {name}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found!")
        else:
            contact_list = "Contacts:\n\n"
            for name, details in self.contacts.items():
                contact_list += f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n\n"
            messagebox.showinfo("Contacts", contact_list)

def main():
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
